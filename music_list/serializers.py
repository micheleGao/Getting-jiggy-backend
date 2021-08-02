from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Artist, Song, Review

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs= serializers.HyperlinkedRelatedField(
        view_name= 'song_detail',
        many= True,
        read_only = True
    )
    artist_url=serializers.ModelSerializer.serializer_url_field(view_name='artist_detail')
    class Meta:
        model = Artist
        fields = ('id', 'photo_url','artist_url', 'nationality', 'name', 'songs')

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

    artist_name = serializers.SlugRelatedField(
        queryset=Artist.objects.all(), slug_field='name', source='artist')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'artist', 'title', 'artist_id',
                  'body', 'created', 'artist_name', 'owner')
