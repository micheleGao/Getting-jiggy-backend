from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # localhost:8000/artist
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    #localhost:8000/artist/ followed by a number would route it to the view being defined
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    #localhost:8000/songs
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
]