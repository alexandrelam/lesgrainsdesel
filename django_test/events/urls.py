from django.urls import path

from . import views

urlpatterns = [
    path('<id>', views.home, name='home'),
]
