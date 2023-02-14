from django.urls import path
from .views import scan,search

urlpatterns = [
    path("", search, name='search'),
    path("scan/",scan, name="scan")
    
]
