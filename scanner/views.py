from django.shortcuts import render
from .models import Rack,Sample
from .forms import RackSelectForm
# Create your views here.




def scan(request):
    
    
    
    return render(request=request, template_name='scan.html')

def search(request):
    return render(request, 'search.html')


