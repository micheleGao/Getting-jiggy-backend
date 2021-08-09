from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Artist, Song, Review

class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail', 
        read_only=True
    )
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset= Artist.objects.all(),
        source = 'artist'
    )
    class Meta:
        model = Song
        fields = ('id', 'artist', 'artist_id', 'title', 'album', 'play_url')
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail', read_only=True)

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source='artist')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'artist', 'title','artist_id',
                  'body', 'created', 'owner')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs= SongSerializer(
        many= True,
        read_only = True
    )
    reviews=ReviewSerializer(
        many=True, 
        read_only =True
    )
    artist_url=serializers.ModelSerializer.serializer_url_field(view_name='artist_detail')
    class Meta:
        model = Artist
        fields = ('id', 'photo_url','artist_url', 'nationality', 'name','reviews', 'songs')




