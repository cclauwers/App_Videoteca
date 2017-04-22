from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView

from Videoteca.models import *

class LoginRequiredMixin(object):
    """Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Videoteca ',
        'pagetitle': 'Welcome to Videoteca ',
        'contentbody': 'A new page made in Spain since 2017',
        'user': request.user,
        'main':'true',
    })
    output = template.render(variables)
    return HttpResponse(output)

#MOVIE
class MovieDetail(generic.DetailView,LoginRequiredMixin):
    model = Movie
    template_name ="movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        return context

class MovieList(generic.ListView,LoginRequiredMixin ):
    model = Movie
    template_name = 'movie_list.html'
    queryset = Movie.objects.all()

#ACTOR

class ActorList(generic.ListView,LoginRequiredMixin):
    model = Actor
    template_name = 'actors_list.html'
    queryset = Actor.objects.all()

class ActorDetail(generic.DetailView,LoginRequiredMixin):
    model = Actor
    template_name = 'actor_detail.html'

#CLIENT

class ClientList(generic.ListView,LoginRequiredMixin):
    model = Client
    template_name = 'clients_list.html'
    queryset = Client.objects.all()

class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'

#VIDEOTECA

class VideotecaList(generic.ListView,LoginRequiredMixin):
    model = Videoteca
    template_name = 'videotecas_list.html'
    queryset = Videoteca.objects.all()

class VideotecaDetail(generic.DetailView,LoginRequiredMixin):
    model = Videoteca
    template_name = 'videoteca_detail.html'




