from django.shortcuts import render, get_object_or_404
from .models import Movies

def movies_list(request):
    movies= Movies.objects.all()
    return render(request,"movies_list.html",{'movies':movies})

def movie_detail(request,movie_id):
    movie = get_object_or_404(Movies,pk=movie_id)
    return render(request,"movie_detail.html",{'movie':movie})








# Create your views here.
