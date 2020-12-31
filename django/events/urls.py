from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_view, name='home'),
    path('events/<id>', views.home),
    path('create/', views.create_events, name="create_events"),
    path('participations/', views.participations, name="participations"),
]
