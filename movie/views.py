# from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q

from .models import Movie


def index(request):
    return render_to_response("movie/index.html")


# search view
def search(request):
    print("searching")
    if request.is_ajax():
        q = request.GET.get("q")
        if q is not None:
            results = Movie.objects.filter(Q(film__contains=q))
            return render_to_response(
                "movie/results.html",
                {"results": results}
            )
