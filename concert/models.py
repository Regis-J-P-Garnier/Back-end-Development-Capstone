from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
CHARFIELD_LEN = 255
LONG_CHARFIELD_LEN = 1000

class Concert(models.Model):
    """concert model"""
    concert_name = models.CharField(max_length=CHARFIELD_LEN)
    duration = models.IntegerField()
    city = models.CharField(max_length=CHARFIELD_LEN)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.concert_name
    
class Photo(models.Model):
    """photo model"""
    id = models.IntegerField(primary_key=True)
    pic_url = models.CharField(max_length=LONG_CHARFIELD_LEN)
    event_country = models.CharField(max_length=CHARFIELD_LEN)
    event_state = models.CharField(max_length=CHARFIELD_LEN)
    event_city = models.CharField(max_length=CHARFIELD_LEN)
    event_date = models.DateField(default=datetime.now)

    class Meta:
        managed = False

    def __str__(self):
        return self.pic_url


class Song(models.Model):
    """song model"""
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=CHARFIELD_LEN)
    lyrics = models.TextField()

    class Meta:
        managed = False

    def __str__(self):
        return self.title


class ConcertAttending(models.Model):
    class AttendingChoices(models.TextChoices):
        NOTHING = "-", _("-")
        NOT_ATTENDING = "Not Attending", _("Not Attending")
        ATTENDING = "Attending", _("Attending")

    concert = models.ForeignKey(
        Concert, null=True, on_delete=models.CASCADE, related_name="attendee"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    attending = models.CharField(
        max_length=100,
        choices=AttendingChoices.choices,
        default=AttendingChoices.NOTHING,
    )

    class Meta:
        unique_together = ['concert', 'user']

    def __str__(self):
        return self.attending
