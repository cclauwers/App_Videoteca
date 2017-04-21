from django.forms import ModelForm
from Videoteca.models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user',)

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        exclude = ('user',)

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)

class VideotecaForm(ModelForm):
    class Meta:
        model = Videoteca
        exclude = ('user',)
