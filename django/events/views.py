from django.shortcuts import render, redirect
from .models import Event, Participation, Adherent
from django.contrib.auth.decorators import login_required
from .utils import formatTime

# Create your views here.


@login_required(login_url='/login/')
def home(request, id):
    if Event.objects.count():
        sorted_events_list = Event.objects.order_by('date_begin')
        context = {'eventsList': sorted_events_list}
        context["selected"] = Event.objects.get(id=id)
        context["participation"] = Participation.objects.filter(event__id=id)
    else:
        context = {}

    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(
        user__id=current_user.id)[0]
    context["page"] = "home"
    return render(request, 'events/details.html', context)


@login_required(login_url='/login/')
def create_events(request):
    context = {}
    current_user = request.user
    context["current_user"] = current_user
    context["adherent"] = Adherent.objects.all().filter(
        user__id=current_user.id)[0]
    context["page"] = "create_events"

    context["eventsList"] = Event.objects.filter(
        author_id=current_user.id).order_by("date_begin")

    if request.method == 'POST':
        titre = request.POST["titre"]
        description = request.POST["description"]
        time_start = request.POST["time-start"]
        time_end = request.POST["time-end"]
        img_icon = None
        img_couverture = None
        author_id = request.user.id
        if len(request.FILES):
            img_icon = request.FILES["img-icon"]
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

    return render(request, 'events/create_events.html', context)


@login_required(login_url='/login/')
def create_events_details(request, id):
    context = {}
    current_user = request.user
    context["current_user"] = current_user
    context["page"] = "create_events"
    context["eventsList"] = Event.objects.filter(
        author_id=current_user.id).order_by("date_begin")
    context["adherent"] = Adherent.objects.all().filter(
        user__id=current_user.id)[0]
    context["event_id"] = id

    if Event.objects.count():
        context["selected"] = Event.objects.get(id=id)

    return render(request, 'events/create_details.html', context)


@login_required(login_url='/login/')
def delete_events(request, id):
    current_obj = Event.objects.get(pk=id)
    if request.user.id == current_obj.author_id:
        current_obj.delete()
    return redirect("/create/")


@login_required(login_url='/login/')
def create_modify_event(request, id):
    context = {}
    current_user = request.user
    context["current_user"] = current_user
    context["page"] = "create_events"
    context["current_event"] = Event.objects.get(pk=id)
    context["current_event_date_begin"] = formatTime(
        Event.objects.get(pk=id).date_begin)
    context["current_event_date_end"] = formatTime(
        Event.objects.get(pk=id).date_end)
    context["modify"] = True
    context["eventsList"] = Event.objects.filter(
        author_id=current_user.id).order_by("date_begin")

    if request.method == 'POST':
        titre = request.POST["titre"]
        description = request.POST["description"]
        time_start = request.POST["time-start"]
        time_end = request.POST["time-end"]
        img_icon = None
        img_couverture = None
        author_id = request.user.id
        if len(request.FILES):
            img_icon = request.FILES["img-icon"]
            img_couverture = request.FILES["img-couverture"]

        if titre and description and time_start and time_end:
            event = Event.objects.get(pk=id)
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
            return redirect("/create/")

    if request.user.id == Event.objects.get(pk=id).author_id:
        return render(request, "events/create_events.html", context)
    else:
        return redirect("/create/")


@login_required(login_url='/login/')
def participations(request):
    context = {}
    context["page"] = "participations"
    return render(request, 'events/participations.html', context)


@login_required(login_url='/login/')
def redirect_view(request):
    if(Event.objects.all()):
        first_event_id = Event.objects.order_by('date_begin').first().id
        response = redirect("events/" + str(first_event_id))
    else:
        response = redirect("events/")
    return response


@login_required(login_url='/login')
def noEvents(request):
    context = {"page": "home"}
    return render(request, 'events/events_list.html', context)


@login_required(login_url='/login/')
def admin_page(request):
    context = {}
    context["page"] = "admin"
    return render(request, 'events/admin_page.html', context)
