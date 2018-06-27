from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib import admin

from django.http import HttpResponse
from rest_framework.urlpatterns import format_suffix_patterns

from movies import views

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls, name='admin'),

    # For API View
    url(r'^movies/', views.movieslist.as_view(), name='movies'),
    url(r'^search-movies/(.*)/', views.MovieSearchInList.as_view(), name='search_movie'), # (.*) should be replaced with a movie name or word which need to match

    # from JSOn file to db
    url(r'^load_movies', views.load_movies, name='load_movies'),

    # for UI-Front View
    url(r'^$', views.home, name='home'),
    url(r'^all_movies', views.all_movies, name='all_movies'),
    url(r'^search_movie', views.search_movies, name='search_movies'),
]
