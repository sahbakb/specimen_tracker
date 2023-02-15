from django.urls import path
from .views import scan,search, rack_select, RackListView, rackDetailView

urlpatterns = [
    path("", search, name='search'),
    path("racks/",rack_select, name="racks"),
    path("racks/<int:pk>/", scan, name='scan'),
    path("racks_list/",RackListView.as_view(), name='racks_list'),
    path("racks_list/<int:pk>",rackDetailView, name='rack_detail' )
    
    
    
    
]
