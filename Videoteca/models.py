from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

class Actor(models.Model):
    name = models.TextField(max_length=50)
    birthYear = models.IntegerField()
    birthPlace = models.TextField(max_length=50)
    biography = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('Videoteca:actor_detail', kwargs={'pk': self.pk})

class Movie(models.Model):
    title = models.TextField(max_length=50)
    year = models.IntegerField()
    duration = models.IntegerField()
    tipus = (('comedy', 'comedy'), ('action', 'action'), ('drama', 'drama'), ('terror', 'terror'),
             ('fantasy', 'fantasy'), ('thriller', 'thriller'), ('aventura', 'aventura'),
             ('scienceFiction', 'scienceFiction'),
             ('western', 'western'))
    genre = models.CharField(max_length=15, choices=tipus, unique=True)
    description = models.TextField(blank=True, null=True)
    actors = models.ManyToManyField(Actor)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('Videoteca:movie_detail', kwargs={'pk': self.pk})

class Client(models.Model):
    DNI = models.TextField(max_length=50)
    name = models.TextField(max_length=50)
    phone = models.IntegerField()
    email = models.TextField(max_length=50)

    def __unicode__(self):
        return u"%s" % self.DNI

    def get_absolute_url(self):
        return reverse('Videoteca:client_detail', kwargs={'pk': self.pk})

class Videoteca(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1
    )
    data_lloguer = models.DateField()
    data_limit = models.DateField()
    movies = models.ManyToManyField(Movie)

    def __unicode__(self):
        return u"%s" % self.client

    def get_absolute_url(self):
        return reverse('Videoteca:videoteca_detail', kwargs={'pk': self.pk})