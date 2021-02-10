from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_view, name='home'),
    path('events/<id>', views.home),
    path('events/', views.noEvents),
    path('create/<id>', views.create_events_details,
         name="create_events_details"),
    path('create/modify/<id>', views.create_modify_event,
         name="create_modify_event"),
    path('create/delete/<id>', views.delete_events, name="delete_events"),
    path('create/', views.create_events, name="create_events"),
    path('inscription_participation/<id>',
         views.inscription_participation, name="inscription_participation"),
    path('desinscription_participation/<id>',
         views.desinscription_participation, name="desinscription_participation"),
    path('participations/<id>', views.participations),
    path('participations/', views.noParticipations),
    path('participations_redirect',
         views.participations_redirect, name="participations"),
    path('admin_details/', views.noEventsAdmin),
    path('admin_redirect/', views.admin_redirect, name="admin_page"),
    path('admin_details/<id>', views.admin_details, name="admin_page"),
    path('admin_validate_event/<id>', views.admin_validate_event, name="validate_event"),
    path('set_en_cours_event/<id>', views.admin_en_cours_event, name="set_en_cours_event"),
    path('set_end_event/<id>', views.admin_end_event, name="set_end_event"),
]
