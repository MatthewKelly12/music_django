from django.http import HttpResponse
from django.shortcuts import render
from .models import Artist
from .models import Song
# from django.urls import render


def index(request):
    return HttpResponse("History!")


def artist_name(request):
    artist_list = Artist.objects.order_by('name_text')
    context = {'artist_list': artist_list}
    return render(request, 'history/artist.html', context)


def song_title  (request):
    song_list = Song.objects.order_by('title_text')
    context = {'song_list': song_list}
    return render(request, 'history/songs.html', context)

def both(request):
    song_list = Song.objects.order_by('title_text')
    context = {'song_list': song_list}
    return render(request, 'history/both.html', context)

