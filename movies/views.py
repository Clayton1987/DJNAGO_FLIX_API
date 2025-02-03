from rest_framework import generics
from movies.models import Movie

from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    print(queryset)
    for item in queryset:
        print(item, item.id)
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

