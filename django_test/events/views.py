from django.shortcuts import render
from .models import Event
# Create your views here.


def home(request):
    sorted_events_list = Event.objects.order_by('date_begin')
    context = {'eventsList': sorted_events_list}
    return render(request, 'events/details.html', context)
