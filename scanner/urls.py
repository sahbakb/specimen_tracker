from django.urls import path
from .views import scan,search, rack_select

urlpatterns = [
    path("", search, name='search'),
    path("racks/",rack_select, name="racks"),
    path("racks/<int:pk>/", scan, name='scan')
    
    
    
]
