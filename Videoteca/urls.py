from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout

from views import *

urlpatterns = [

    #LOGIN -> /Videoteca/login/
    #url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'login.html'}),
    #url(r'^logout/$', auth_views.logout, kwargs={'template_name': 'mainpage.html'}, name='logout'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/successfully_logged_out/'}),


    # MOVIE -> List Movies: /Videoteca/movies
    url(r'^movies/$',MovieList.as_view(),name='movie_list'),
    # Movie detail: /Videoteca/movies/1
    url(r'^movies/(?P<pk>\d+)/$',MovieDetail.as_view(model = Movie,template_name = 'movie_detail.html'),name='movie_detail'),

    #ACTOR -> List actors: /Videoteca/actors
    url(r'^actors/$',ActorList.as_view(),name='actors_list'),
    # actor detail: /Videoteca/actors/1
    url(r'^actors/(?P<pk>\d+)/$',ActorDetail.as_view(model = Actor,template_name = 'actor_detail.html'),name='actor_detail'),

    # Client -> List clients: /Videoteca/clients
    url(r'^clients/$', ClientList.as_view(), name='clients_list'),
    # client detail: /Videoteca/clients/1
    url(r'^clients/(?P<pk>\d+)/$', ClientDetail.as_view(model=Client, template_name='client_detail.html'),name='client_detail'),

    # Videoteca -> List videotecas: /Videoteca/videotecas
    url(r'^videotecas/$', VideotecaList.as_view(), name='videotecas_list'),
    # Videoteca detail: /Videoteca/videoteca/1
    url(r'^videotecas/(?P<pk>\d+)/$', VideotecaDetail.as_view(model=Videoteca, template_name='videoteca_detail.html'),name='videoteca_detail'),

]