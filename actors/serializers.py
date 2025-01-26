from rest_framework import serializers
from actors.models import Actor

class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        #fields = ('id', 'name', 'age', 'gender')  # fields to b
        fields = '__all__'  # all fields