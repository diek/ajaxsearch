from django.contrib import admin
from .models import Director, Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_dispay = ("director")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_dispay = (
        'entry',
        'film',
        'director',
        'leading_actor',
        'year_release',
        'oscars',
        'imdb_link',
        'guardian_page',
        'country',
        'genre',
    )
