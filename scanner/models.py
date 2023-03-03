from django.db import models
import datetime

# Create your models here.


class SampleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rack(models.Model):
    
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    sample_type = models.ForeignKey(SampleType, on_delete=models.CASCADE)
    rack_size = models.IntegerField(default=72, null=False, blank=False)
    next_available_position = models.IntegerField(default=1)
    full = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

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
