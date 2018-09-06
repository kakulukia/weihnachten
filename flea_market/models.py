from uuid import uuid4

import pendulum
from constance import config
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Sum
from django.template.defaultfilters import date as date_format
from django.utils.translation import activate
from django_undeletable.models import BaseModel, DataManager
from post_office import mail


class Event(BaseModel):
    start = models.DateTimeField('Start')
    name = models.CharField(max_length=100, default='')
    location = models.TextField(default='')
    location_size = models.IntegerField(default=1)
    for_schools = models.BooleanField('Für (Vor-)Schulkinder', default=True)

    class Meta(BaseModel.Meta):
        verbose_name = 'Veranstaltung'
        verbose_name_plural = 'Veranstaltungen'
        ordering = ['start']

    def __str__(self):
        return f'Veranstaltung vom {date_format(self.start, "d.m.Y")}'

    def cancel_date(self):
        return pendulum.instance(self.start).start_of('day').subtract(days=config.MARKET_CANCEL_DURATION)

    @property
    def available_places(self):
        places = self.inquiries.aggregate(kids=Sum('kids'), adults=Sum('adults'))
        return self.location_size - (places['kids'] or 0) - (places['adults'] or 0)


class InquiryDataManager(DataManager):
    pass


class Inquiry(BaseModel):
    first_name = models.CharField("Vorname", max_length=50)
    last_name = models.CharField("Nachname", max_length=50)
    email = models.EmailField("E-Mail")
    phone = models.CharField("Telefonnummer", max_length=50)
    class_name = models.CharField('Schule / Klasse', max_length=150, default='')
    kids = models.IntegerField('Anzahl Kinder')
    adults = models.IntegerField('Anzahl Erwachsene')

    paid = models.BooleanField("Bezahlt", default=False)

    event = models.ForeignKey(
        'flea_market.Event', verbose_name="Veranstaltung", related_name='inquiries',
        on_delete=models.CASCADE)

    data = InquiryDataManager()

    class Meta(BaseModel.Meta):
        ordering = [
            '-paid',
            'created',
        ]
        verbose_name = 'Anfrage'
        verbose_name_plural = 'Anfragen'

    def __str__(self):
        return self.name

    @property
    def name(self):
        return " ".join([self.first_name, self.last_name])

    def send_mail(self, template, extra_context=None, notify_admins=False):
        if notify_admins:
            receiver = [r.strip() for r in config.ADMINS.split(',')]
        else:
            receiver = self.email
        if settings.EMAIL_OVERRIDE_ADDRESS:
            receiver = settings.EMAIL_OVERRIDE_ADDRESS

        context = {
            'user': " ".join([self.first_name, self.last_name]),
            'inquiry': self
        }
        if extra_context:
            context.update(extra_context)

        activate('de')
        mail.send(
            receiver,
            settings.DEFAULT_FROM_EMAIL,
            template=template,
            context=context,
        )

    def accept(self):

        context = {
            'cancel_url': 'http://{}/cancel-market-inquiry/{}'.format(
                Site.objects.get_current().domain,
                self.token
            ),
        }

        self.send_mail('confirm_flea_market_inquiry', context)

        self.chosen = True
        self.save()

    def cancel_date(self):
        return self.event.cancel_date()

    def validate_email(self):
        self.email_valid = True
        self.save()

    def cancel(self):
        self.canceled = True
        self.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if not self.id:
            self.send_mail('confirm_inquiry')
            self.send_mail('new_inquiry', notify_admins=True)
        else:
            if self.paid and not Inquiry.data.filter(id=self.id, paid=True).exists():
                self.send_mail('confirm_payment', notify_admins=True)

        super().save(force_insert, force_update, using, update_fields)

    def mark_permanent(self):
        self.permanent_seller = True
        self.save()

    def reset(self, new_event):
        # resets this instance and saves it as a fresh version for
        # the given event, email will stay validated
        self.id = None
        self.event_id = new_event.id
        self.chosen = False
        self.blocked = False
        self.canceled = False
        self.token = uuid4()

        self.save()

    def make_permanent(self, yes_no):
        self.permanent_seller = yes_no
        self.save()
