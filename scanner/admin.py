from django.contrib import admin
from .models import SampleType, Sample, Rack
# Register your models here.


@admin.register(SampleType)
class SampleTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['sid', 'rack', 'location', 'time_scanned']
    list_filter = ['rack','time_scanned']


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    pass
