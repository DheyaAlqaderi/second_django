from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie


def movies(request):
  
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Hello World")

def detail(request, id):
    try:
        data = Movie.objects
        data = data.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    name1 = request.POST.get('name')

    if name1:
        movie = Movie(name=name1)
        movie.save()
        return HttpResponseRedirect('/movies/')
    return render(request, 'movies/add.html')


def delete(request, id):
    try:
        movie = get_object_or_404(Movie, pk=id)
        movie.delete()
        return redirect('/movies')  # Assuming you have a named URL for movies list
    except Http404:
        return render(request, 'movies/404.html')  # Customize this template as needed
    