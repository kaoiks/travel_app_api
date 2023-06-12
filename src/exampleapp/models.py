from django.db import models
from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=64, unique=True, help_text="user full name")
    role = models.CharField(max_length=32, blank=True, null=True, help_text="user role")

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=128, help_text="Task description")


class Ticket(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_field = models.FileField(upload_to='media_files/', null=True, blank=True)
    travel_date = models.DateTimeField(auto_now=True)
    start_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, related_name='start_tickets')
    end_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, related_name='end_tickets')


class Location(models.Model):
    name = models.CharField(max_length=250, help_text="Location Name")
    latitude = models.CharField(max_length=100, help_text="Location latitude")
    longitude = models.CharField(max_length=100, help_text="Location longitude")
