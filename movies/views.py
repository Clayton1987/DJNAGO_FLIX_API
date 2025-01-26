from rest_framework import generics
from movies.models import Movie

from movies.serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    print(queryset)
    for item in queryset:
        print(item, item.id)
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

