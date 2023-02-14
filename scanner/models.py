from django.db import models

# Create your models here.

class SampleType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Rack(models.Model):
    name = models.CharField(max_length=50)
    sample_type = models.ForeignKey(SampleType, on_delete=models.CASCADE)
    rack_size = models.IntegerField(default=72)
    next_available_position = models.IntegerField(default=1)
    full = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}, {self.sample_type}"
    
    
    
class Sample(models.Model):
    sid = models.CharField(max_length=20)
    time_scanned = models.DateTimeField(auto_now_add=True)
    rack = models.ManyToManyField(Rack)   
    location=models.IntegerField()    
    def __str__(self):
        return self.sid
