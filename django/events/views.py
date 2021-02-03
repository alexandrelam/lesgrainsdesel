from django.shortcuts import render, redirect
from .models import Event, Participation, Adherent
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home(request, id):
    if Event.objects.count() != 0:
        sorted_events_list = Event.objects.order_by('date_begin')
        context = {'eventsList': sorted_events_list}
        context["selected"] = Event.objects.get(id=id)
        context["participation"] = Participation.objects.filter(event__id=id)
    else:
        context = {}
    
    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(user__id=current_user.id)[0]
    context["page"] = "home"
    return render(request, 'events/details.html', context)

@login_required(login_url='/login/')
def create_events(request):
    context = {}
    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(user__id=current_user.id)[0]
    context["page"] = "create_events"
    return render(request, 'events/create_events.html', context)

@login_required(login_url='/login/')
def participations(request):
    context = {}
    context["page"] = "participations"
    return render(request, 'events/participations.html', context)

@login_required(login_url='/login/')
def redirect_view(request):
    response = redirect("events/1")
    return response
