from django.http import HttpResponse
# from django.urls import render


def index(request):
    return HttpResponse("History!")
    # artist_list = Artist.objects.order_by('name_text')
    # context = {'artist_list': artist_list}
    # return render(request, 'history/index.html', context)


def artist_name(request):
    return HttpResponse("What's up?!")
    # return HttpResponse(artist_id)

def song_title  (request):
    return HttpResponse("Up!")
    # return HttpResponse(song_id)
