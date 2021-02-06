from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_view, name='home'),
    path('events/<id>', views.home),
    path('events/', views.noEvents),
    path('create/<id>', views.create_events_details,
         name="create_events_details"),
    path('create/', views.create_events, name="create_events"),
    path('participations/', views.participations, name="participations"),
    path('admin_page/', views.admin_page, name="admin_page"),
]
