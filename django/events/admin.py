from django.contrib import admin
from .models import Event, Participation, Adherent

admin.site.register(Event)
admin.site.register(Participation)
admin.site.register(Adherent)
