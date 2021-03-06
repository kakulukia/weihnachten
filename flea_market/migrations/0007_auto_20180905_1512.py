# Generated by Django 2.1 on 2018-09-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0006_auto_20180905_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'base_manager_name': 'data', 'default_manager_name': 'data', 'get_latest_by': 'created', 'ordering': ['start'], 'verbose_name': 'Veranstaltung', 'verbose_name_plural': 'Veranstaltungen'},
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='class_name',
            field=models.CharField(max_length=150, verbose_name='Schule / Klasse'),
        ),
    ]
