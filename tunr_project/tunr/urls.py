# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
    path('artists/new', views.artist_create, name='artist_create'),
    path('songs/new', views.song_create, name='song_create'),
]

