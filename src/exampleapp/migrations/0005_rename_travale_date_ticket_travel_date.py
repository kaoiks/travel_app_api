# Generated by Django 4.0 on 2023-06-09 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exampleapp', '0004_ticket_travale_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='travale_date',
            new_name='travel_date',
        ),
    ]
