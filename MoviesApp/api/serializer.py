from rest_framework import serializers
from MoviesApp.models import Movie_Rate , Movie , MovieSerial

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    detail = serializers.CharField(max_length=200)
    trailer_url = serializers.URLField()
    director = serializers.CharField()
    genere = serializers.CharField()



class MovieSerializerRest(serializers.ModelSerializer):
    title_movie = serializers.CharField()
    detail_movie = serializers.CharField()
    trailer_url = serializers.CharField()
    #director = serializers.StringRelatedField()


    class Meta:
        model = MovieSerial
        fields = ('title_movie' , 'detail_movie' , 'trailer_url')


