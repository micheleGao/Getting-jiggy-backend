from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, default='no song title')
    album = models.CharField(max_length=100, default='no album title')
    play_url = models.CharField(max_length=200, null=True)

    def __str__(self):
      return self.title

class Review(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artist')
    body = models.TextField()
    # author= models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
