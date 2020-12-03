from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_view),
    path('events/<id>', views.home, name='home'),
]
