from django.contrib import admin

# Register your models here.

from .models import Equipos
from .models import Jugadores
from .models import Estadios

admin.site.register(Equipos)
admin.site.register(Jugadores)
admin.site.register(Estadios)
