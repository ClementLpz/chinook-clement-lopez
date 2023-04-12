from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Track, Artist, Album

def album(request):
    album_list = Album.objects.order_by('title')
    context = {'album_list': album_list}
    return render(request, 'disks/album.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'disks/detail.html', context)

def search_album(request):
    form = AlbumForm(request.GET)
    album_filtered_list = Album.objects.filter(title__contains='a') # Just a test for the 'contains', I want to put title__contains=form
    context = {'album_filtered_list': album_filtered_list}
    return render(request, 'disks/album.html', context)
