# Generated by Django 4.0 on 2023-06-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleapp', '0003_alter_ticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='travale_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]