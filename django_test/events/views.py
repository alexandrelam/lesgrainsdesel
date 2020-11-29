from django.shortcuts import render
from .models import Event
# Create your views here.


def home(request, id):
    sorted_events_list = Event.objects.order_by('date_begin')
    context = {'eventsList': sorted_events_list}
    context["selected"] = Event.objects.get(id=id)
    return render(request, 'events/details.html', context)
