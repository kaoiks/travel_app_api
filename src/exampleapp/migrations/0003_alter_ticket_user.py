# Generated by Django 4.0 on 2023-06-09 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('exampleapp', '0002_location_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
