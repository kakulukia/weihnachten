from django.contrib import admin

# Register your models here.
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from flea_market.models import Inquiry, Event


@admin.register(Inquiry)
class MarketInquiryAdmin(admin.ModelAdmin):
    list_display = ['created', 'first_name', 'last_name', 'email', 'phone', 'class_name', 'paid']
    list_filter = ['event', 'paid']
    search_fields = ['first_name', 'last_name']
    actions = None


@admin.register(Event)
class MarketEventAdmin(admin.ModelAdmin):
    list_display = ['start', 'available_places', 'download_list']
    actions = None

    def download_list(self, obj):
        button = f'<a class="button" href="/api/events/{obj.id}/download"> Gästeliste</a>'
        return mark_safe(button)
    download_list.short_description = "Gästeliste runterladen"

