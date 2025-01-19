from django.shortcuts import render
from django.http import JsonResponse
from genres.models import Genre

# Create your views here.
def genre_view(request):
    #return render(request, 'genre.html')
    genres = Genre.objects.all()
    data = [{'id': genre.id, 'name': genre.name} for genre in genres]
    return JsonResponse(data, safe=False)