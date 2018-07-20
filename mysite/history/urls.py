from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
      path('', views.index, name='index'),
      path('artists', views.artist_name, name='artist_name'),
      path('songs', views.song_title, name='song_title')

    #   path('', 'views.artist_name', name='artist'),
    # ex: /polls/5/results/
    # path('', views.history_song, name='song_title')
]

