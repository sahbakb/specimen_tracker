from django.db import models
import datetime

# Create your models here.


class SampleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rack(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wedesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]

    name = models.CharField(max_length=50,
                            null=False, blank=False)
    day = models.CharField(max_length=10, blank=False,
                           null=False, choices=DAY_CHOICES, default='Monday')
    sample_type = models.ForeignKey(SampleType, on_delete=models.CASCADE)
    rack_size = models.IntegerField(default=72, null=False, blank=False)
    next_available_position = models.IntegerField(default=1)

    full = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day},{self.sample_type},{self.name}"

    def get_available_spots(self):
        return self.rack_size - self.next_available_position + 1
    get_available_spots.short_description = "available_spots"


class Sample(models.Model):
    sid = models.CharField(max_length=20)
    time_scanned = models.DateTimeField(auto_now_add=True)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    location = models.IntegerField()

    def __str__(self):
        return self.sid
