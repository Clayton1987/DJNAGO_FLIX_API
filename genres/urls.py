from django.contrib import admin
from django.urls import path
#from . import views
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView, genre_create_list_view, genre_detail_view



urlpatterns = [
  
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    #path('genres/<int:pk>/', genre_detail_view , name='genre-detail-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view() , name='genre-detail-view'),
]
