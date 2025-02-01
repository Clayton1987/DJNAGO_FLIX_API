from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from reviews.models import Review
from actors.models import Actor
from django.db.models import Avg

class MovieSerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all()
    )
    relase_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    resume = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Movie
        fields = '__all__'  # all fields
    
    def get_rate(self,obj):
        #return obj.get_rate()  # return the rate of the movie
        # reviews = obj.reviews.all()
        # if reviews:
        #     sum_reviews =0
        #     for review in reviews:
        #         sum_reviews += review.stars
        #         print(sum_reviews)
        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 2)
        # return None
        #### NEW VERSION
        #obj.reviews.aggregate(Avg('stars')) # TODOS CAMPOS
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg'] #MEDIA CADA UM OBJ
        if rate:
            return round(rate, 2)
        return None

        
    
    def validate(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('Movie is too old')
        return value
    
    def validade_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resume is too long')
        return value
    