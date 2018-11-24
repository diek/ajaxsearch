from django.urls import path
from . import views


app = 'movie'

urlpatterns = [
    path('', views.index, name='search_ingredients'),
    path('search/', views.search, name='search'),
]
