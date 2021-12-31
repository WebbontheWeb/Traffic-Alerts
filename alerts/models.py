from django.db import models

# Create your models here.
class Trip(models.Model):
    toAddress = models.CharField(max_length=100)
    fromAddress = models.CharField(max_length=100)
    arrivalTime = models.TimeField()
    bufferMinutes = models.IntegerField()
    nextTrip = models.DateField()
    repeatsMonday = models.BooleanField()
    repeatsTuesday = models.BooleanField()
    repeatsWednesday = models.BooleanField()
    repeatsThursday = models.BooleanField()
    repeatsFriday = models.BooleanField()
    repeatsSaturday = models.BooleanField()
    repeatsSunday = models.BooleanField()
    notificationEmail = models.EmailField()
