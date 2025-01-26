from rest_framework import generics
from reviews.models import Review 

from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    print(queryset)
    for item in queryset:
        print(item, item.id)
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

