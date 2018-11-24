from django.urls import path
from . import views


app = 'movie'

urlpatterns = [
    path('movie/', views.index, name='movie'),
    path('search/', views.search, name='search'),
]
