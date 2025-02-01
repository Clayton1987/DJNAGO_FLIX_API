from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView 
	
	


urlpatterns = [
	# path('hello/', hello_view),
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view() , name='actor-detail-view'),
   
]
