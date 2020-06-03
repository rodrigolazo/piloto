from django.forms import ModelForm
from aplicacion1.models import Persona

class FormularioPersonas(ModelForm):
    class Meta:
        model = Persona
        fields =['nombre','edad','aficion']