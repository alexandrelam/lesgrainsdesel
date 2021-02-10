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
    path('admin_next_status/<id>', views.admin_next_status, name="admin_next_status"),
    path('admin_previous_status/<id>', views.admin_previous_status, name="admin_previous_status"),
]
