from django import forms

from .models import Equipos
from .models import Jugadores
from .models import Estadios

class FormCreate_Equipos(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = "__all__"

class FormCreate_Jugadores(forms.ModelForm):
    class Meta:
        model = Jugadores
        fields = "__all__"

class FormCreate_Estadios(forms.ModelForm):
    class Meta:
        model = Estadios
        fields = "__all__"
