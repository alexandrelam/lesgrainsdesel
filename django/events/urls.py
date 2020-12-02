from django.urls import path

from . import views

urlpatterns = [
    path('events/<id>', views.home, name='home'),
]
