from django.http import HttpResponse
from django.shortcuts import render
from .models import Artist
# from django.urls import render


def index(request):
    return HttpResponse("History!")


def artist_name(request):
    artist_list = Artist.objects.order_by('name_text')
    print(artist_list)
    context = {'artist_list': artist_list}
    return render(request, 'history/artist.html', context)


def song_title  (request):
    return HttpResponse("Up!")
    # return HttpResponse(song_id)
