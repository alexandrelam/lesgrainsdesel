from django.shortcuts import render, redirect
from .models import Event, Participation, Adherent
from django.contrib.auth.decorators import login_required
from .utils import formatTime
from odoo.odoo import Odoo
from datetime import datetime

# Create your views here.


@login_required(login_url='/login/')
def home(request, id):
    if Event.objects.count():
        sorted_events_list = Event.objects.filter(
            status="VAL").order_by('date_begin')
        context = {'eventsList': sorted_events_list}
        context["selected"] = Event.objects.get(id=id)
        context["participation"] = Participation.objects.filter(event__id=id)
    else:
        context = {}

    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(
        userId=current_user.userId)[0]
    context["page"] = "home"
    context["event_id"] = id
    context["participe"] = False
    if Participation.objects.filter(Adherent__userId=current_user.userId, event__id=id):
        context["participe"] = True
    return render(request, 'events/details.html', context)


@login_required(login_url='/login/')
def create_events(request):
    context = {}
    context["displayStatus"] = True
    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(
        userId=current_user.userId)[0]
    context["page"] = "create_events"

    context["eventsList"] = Event.objects.filter(
        author_id=current_user.userId).order_by("date_begin")

    context["errorMsg"] = False

    if request.method == 'POST':
        titre = request.POST["titre"]
        description = request.POST["description"]
        time_start = request.POST["time-start"]
        time_end = request.POST["time-end"]
        img_icon = None
        img_couverture = None
        author_id = request.user.userId

        if "img-icon" in request.FILES:
            img_icon = request.FILES["img-icon"]

        if "img-couverture" in request.FILES:
            img_couverture = request.FILES["img-couverture"]

        if titre and description and time_start and time_end:
            event = Event()
            event.author_id = author_id
            event.title = titre
            event.short_description = description
            event.long_description = description
            event.date_begin = time_start
            event.date_end = time_end

            if img_icon:
                event.icon = img_icon

            if img_couverture:
                event.image = img_couverture

            event.save()
        else:
            context["errorMsg"] = True

    return render(request, 'events/create_events.html', context)


@login_required(login_url='/login/')
def create_events_details(request, id):
    context = {}
    context["displayStatus"] = True
    current_user = request.user
    context["current_user"] = current_user
    context["page"] = "create_events"
    context["eventsList"] = Event.objects.filter(
        author_id=current_user.userId).order_by("date_begin")
    context["adherent"] = Adherent.objects.all().filter(
        userId=current_user.userId)[0]
    context["event_id"] = id
    context["participation"] = Participation.objects.filter(event__id=id)

    if Event.objects.count():
        context["selected"] = Event.objects.get(id=id)

    return render(request, 'events/create_details.html', context)


@login_required(login_url='/login/')
def delete_events(request, id):
    current_obj = Event.objects.get(pk=id)
    if request.user.userId == current_obj.author_id:
        current_obj.delete()
    return redirect("/create/")


@login_required(login_url='/login/')
def create_modify_event(request, id):
    context = {}

    current_user = request.user
    context["current_user"] = current_user

    context["page"] = "create_events"

    context["current_event"] = Event.objects.get(pk=id)

    context["modify"] = True
    context["displayStatus"] = True
    context["eventsList"] = Event.objects.filter(
        author_id=current_user.userId).order_by("date_begin")

    context["errorMsg"] = False

    if request.method == 'POST':
        titre = request.POST["titre"]
        description = request.POST["description"]
        time_start = request.POST["time-start"]
        time_end = request.POST["time-end"]
        img_icon = None
        img_couverture = None
        author_id = request.user.userId

        if "img-icon" in request.FILES:
            img_icon = request.FILES["img-icon"]

        if "img-couverture" in request.FILES:
            img_couverture = request.FILES["img-couverture"]

        if titre and description:
            event = Event.objects.get(pk=id)
            event.author_id = author_id
            event.title = titre
            event.short_description = description
            event.long_description = description

            if len(time_start) != 0:
                event.date_begin = time_start

            if len(time_end) != 0:
                event.date_end = time_end

            if img_icon:
                event.icon = img_icon

            if img_couverture:
                event.image = img_couverture
            event.save()
            return redirect("/create/")
        else:
            context["errorMsg"] = True

    if request.user.userId == Event.objects.get(pk=id).author_id:
        return render(request, "events/create_events.html", context)
    else:
        return redirect("/create/")


@login_required(login_url='/login/')
def participations(request, id):
    if Event.objects.count():
        sorted_participations_list = Participation.objects.filter(
            Adherent__userId=request.user.userId).order_by('event__date_begin')
        print(sorted_participations_list)
        context = {'participationsList': sorted_participations_list}
        context["selected"] = Event.objects.get(id=id)
        context["participation"] = Participation.objects.filter(event__id=id)
    else:
        context = {}

    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(
        userId=current_user.userId)[0]
    context["page"] = "participations"
    context["event_id"] = id
    context["participe"] = False
    if Participation.objects.filter(Adherent__userId=current_user.userId, event__id=id):
        context["participe"] = True
    return render(request, 'events/participations_details.html', context)


@login_required(login_url='/login/')
def participations_redirect(request):
    if(Participation.objects.filter(Adherent__userId=request.user.userId).order_by("event__date_begin")):
        first_event_id = Event.objects.order_by('date_begin').first().id
        response = redirect("/participations/" + str(first_event_id))
    else:
        response = redirect("/participations/")
    return response


@login_required(login_url='/login/')
def noParticipations(request):
    context = {"page": "participations"}
    context["current_user"] = request.user
    return render(request, "events/events_list.html", context)


@login_required(login_url='/login/')
def redirect_view(request):
    if(Event.objects.filter(status="VAL")):
        first_event_id = Event.objects.filter(
            status="VAL").order_by('date_begin').first().id
        response = redirect("events/" + str(first_event_id))
    else:
        response = redirect("events/")
    return response


@login_required(login_url='/login')
def noEvents(request):
    context = {"page": "home"}
    context["current_user"] = request.user
    return render(request, 'events/events_list.html', context)


@login_required(login_url='/login/')
def inscription_participation(request, id):
    participation = Participation()
    participation.event = Event.objects.get(pk=id)
    adherent_id = Adherent.objects.get(userId=request.user.userId).pk
    participation.Adherent = Adherent.objects.get(pk=adherent_id)
    participation.save()
    return redirect('home')


@login_required(login_url='/login/')
def desinscription_participation(request, id):
    participation = Participation.objects.get(
        Adherent__userId=request.user.userId, event__id=id)
    participation.delete()
    return redirect('home')


@login_required(login_url='/login/')
def admin_redirect(request):
    if(Event.objects.all()):
        first_event_id = Event.objects.order_by('date_begin').first().id
        response = redirect("/admin_details/" + str(first_event_id))
    else:
        response = redirect("/admin_details/")
    return response


@login_required(login_url='/login/')
def admin_details(request, id):
    context = {}
    if Event.objects.count():
        sorted_events_list = Event.objects.order_by('date_begin')
        context = {'eventsList': sorted_events_list}
        context["selected"] = Event.objects.get(id=id)
        context["participation"] = Participation.objects.filter(event__id=id)
    context["page"] = "admin"
    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(
        userId=current_user.userId)[0]
    context["event_id"] = id
    context["participe"] = False
    context["displayStatus"] = True
    if Participation.objects.filter(Adherent__userId=current_user.userId, event__id=id):
        context["participe"] = True
    return render(request, 'events/admin_page.html', context)


@login_required(login_url='/login/')
def noEventsAdmin(request):
    context = {}
    context["page"] = "admin"
    context["current_user"] = request.user
    return render(request, 'events/events_list.html', context)


@login_required(login_url='/login/')
def admin_next_status(request, id):
    current_event = Event.objects.get(pk=id)
    if current_event.status == "ECV":
        current_event.status = "VAL"
    elif current_event.status == "VAL":
        odoo = Odoo('admin', 'admin')
        odoo.connect()
        current_event.status = "TER"
        print("name :"+current_event.title+" date :"+str(current_event.date_begin.strftime(
            "%Y-%m-%d %H:%M:%S"))+" author_id : "+str(current_event.author_id))
        current_event.odoo_id = odoo.sendEventToOdoo(current_event.title, current_event.date_begin.strftime(
            "%Y-%m-%d %H:%M:%S"), current_event.date_begin.strftime("%Y-%m-%d %H:%M:%S"), current_event.author_id)
        print(" odoo event id "+str(current_event.odoo_id))
    current_event.save()
    return redirect("/admin_redirect/")


@login_required(login_url='/login/')
def admin_previous_status(request, id):
    current_event = Event.objects.get(pk=id)
    if current_event.status == "VAL":
        current_event.status = "ECV"
    elif current_event.status == "TER":
        odoo = Odoo('admin', 'admin')
        odoo.connect()
        current_event.status = "VAL"
        odoo.deleteOdooEvent(current_event.odoo_id)

    current_event.save()
    return redirect("/admin_redirect/")
