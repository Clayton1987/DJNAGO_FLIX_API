from rest_framework import serializers
from genres.models import Genre

# class GenrerSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()
#
 
# usando ModelSerializer:
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        #fields = ['id', 'name', 'description']  # campos que serão exibidos
        # read_only_fields = ['id']  # campos que não podem ser alterados
        # extra_kwargs = {'name': {'required': False}}  # campos que podem ser alter
        fields = '__all__'
