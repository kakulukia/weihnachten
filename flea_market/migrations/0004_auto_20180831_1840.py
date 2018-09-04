# Generated by Django 2.1 on 2018-08-31 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0003_inquiry_places'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inquiry',
            options={'base_manager_name': 'data', 'default_manager_name': 'data', 'get_latest_by': 'created', 'ordering': ['-paid', 'created'], 'verbose_name': 'Flohmarktanfrage', 'verbose_name_plural': 'Flohmarktanfragen'},
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='blocked',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='canceled',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='chosen',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='email_valid',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='permanent_seller',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='token',
        ),
        migrations.AddField(
            model_name='inquiry',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Bezahlt'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='flea_market.Event', verbose_name='Veranstaltung'),
        ),
    ]
