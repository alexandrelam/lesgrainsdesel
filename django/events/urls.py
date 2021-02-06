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
    path('participations/', views.participations_redirect, name="participations"),
    path('admin_page/', views.admin_page, name="admin_page"),
]
