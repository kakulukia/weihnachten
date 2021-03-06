# Generated by Django 2.1 on 2018-08-31 12:44

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('start', models.DateTimeField(verbose_name='Start')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('concealed', models.BooleanField(default=False, editable=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Vorname')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nachname')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefonnummer')),
                ('chosen', models.BooleanField(default=False, verbose_name='Ausgewaehlt')),
                ('blocked', models.BooleanField(default=False, verbose_name='Geblockt')),
                ('token', models.CharField(default=uuid.uuid4, max_length=50, verbose_name='AbsageToken')),
                ('canceled', models.BooleanField(default=False, verbose_name='Abgesagt')),
                ('email_valid', models.BooleanField(default=False, verbose_name='E-Mail bestätigt')),
                ('permanent_seller', models.BooleanField(default=False, verbose_name='Dauergast')),
                ('event', models.ForeignKey(limit_choices_to={'flea_market': True}, on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='flea_market.Event', verbose_name='Veranstaltung')),
            ],
            options={
                'verbose_name': 'Flohmarktanfrage',
                'verbose_name_plural': 'Flohmarktanfragen',
                'ordering': ['-email_valid', 'canceled', '-chosen', '-permanent_seller', 'created'],
                'get_latest_by': 'created',
                'abstract': False,
                'base_manager_name': 'data',
                'default_manager_name': 'data',
            },
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
    ]
