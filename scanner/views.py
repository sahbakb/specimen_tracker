from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.urls import reverse_lazy
from .models import Rack, Sample
from django.views.generic import ListView, DetailView
# Create your views here.


def rack_select(request):
    racks = Rack.objects.filter(full=False)

    context = {"racks": racks}
    return render(request=request, template_name='rack_select.html', context=context)


def scan(request, pk):
    rack = Rack.objects.get(id=pk)
    available_spots = []
    for i in range(rack.next_available_position, rack.rack_size+1):
        available_spots.append(i)

    if request.method == 'POST':
        req = request.POST
        
        for i in available_spots:
            if req[str(i)] != '':
                s = Sample()
                s.sid = req[str(i)]

                s.location = i
                s.rack = rack
                rack.next_available_position = rack.next_available_position + 1
                if rack.next_available_position > rack.rack_size:
                    rack.full = True
                elif req["close"] == 'on':
                    rack.full = True
                s.save()
                rack.save()

        return redirect('racks')
    context = {'available_spots': available_spots, "rack": rack}
    return render(request, 'scan.html', context=context)


def search(request):
    if request.method == 'POST':
        req = request.POST
        samples = Sample.objects.filter(sid=req["sid"])
        context = {'samples': samples}
    else:
        context = {}
    return render(request, 'search.html', context=context)


class RackListView(ListView):
    model = Rack
    template_name = 'rack_list.html'
    context_object_name = 'racks'


def rackDetailView(request, pk):
    rack = Rack.objects.get(id=pk)
    samples = rack.sample_set.all()
    context = {"rack": rack, 'samples': samples}
    return render(request, template_name='rack_detail.html', context=context)


def empty_rack(request, pk):
    rack = Rack.objects.get(id=pk)
    samples = rack.sample_set.all()
    if request.method == "POST":
        samples.delete()
        rack.next_available_position = 1
        rack.save()
        return redirect('racks_list')
    else:

        context = {"rack": rack, 'samples': samples}
        return render(request, template_name='empty_rack.html', context=context)
