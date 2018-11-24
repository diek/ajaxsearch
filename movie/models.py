from django.db import models


class Genre(models.Model):
    GENRE_ID = 1
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Director(models.Model):
    DIRECTOR_ID = 1
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.director


class Country(models.Model):
    COUNTRY_ID = 236
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.country


class Movie(models.Model):
    entry = models.SmallIntegerField(default=0)
    film = models.CharField(max_length=100)
    director = models.ForeignKey(Director, models.PROTECT, default=Director.DIRECTOR_ID)
    leading_actor = models.CharField(max_length=300)
    year_release = models.SmallIntegerField(verbose_name="Cinematic Release", null=True, blank=True)
    oscars = models.SmallIntegerField(default=0)
    imdb_link = models.URLField(max_length=100)
    guardian_page = models.URLField(max_length=100)
    country = models.ForeignKey(Country, models.PROTECT, default=Country.COUNTRY_ID)
    genre = models.ForeignKey(Genre, models.PROTECT, default=Genre.GENRE_ID)

    def __str__(self):
        return self.film
