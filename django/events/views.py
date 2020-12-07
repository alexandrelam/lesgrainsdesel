from django.shortcuts import render, redirect
from .models import Event, Participation
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home(request, id):
    sorted_events_list = Event.objects.order_by('date_begin')
    context = {'eventsList': sorted_events_list}
    context["selected"] = Event.objects.get(id=id)
    context["participation"] = Participation.objects.filter(event__id=id)
    context["current_user"] = request.user
    return render(request, 'events/details.html', context)

@login_required(login_url='/login/')
def redirect_view(request):
    response = redirect("events/1")
    return response