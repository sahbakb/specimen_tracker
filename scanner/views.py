from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Rack,Sample
# Create your views here.




def rack_select(request):
    racks = Rack.objects.filter(full=False)
                       
        
    context={"racks":racks}
    return render(request=request, template_name='rack_select.html', context=context)


def scan(request, pk):
    rack = Rack.objects.get(id=pk)
    available_spots = [] 
    for i in range(rack.next_available_position,rack.rack_size+1):
        available_spots.append(i)
    
    if request.method == 'POST':
        req = request.POST
        for i in available_spots:
            if req[str(i)] != '':
                s = Sample()
                s.sid = req[str(i)]
                
                s.location=i
                s.rack = rack
                rack.next_available_position = rack.next_available_position + 1
                if rack.next_available_position > rack.rack_size:
                    rack.full = True
                s.save()
                rack.save()
                
        return redirect('racks')        
    context = {'available_spots':available_spots, "rack":rack}
    return render(request, 'scan.html',context=context)

def search(request):
    return render(request, 'search.html')


