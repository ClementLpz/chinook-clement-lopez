from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Track, Artist, Album
from .forms import AlbumForm

def album(request):

    album_list = Album.objects.order_by('title')

    if request.method == 'GET':
        form = AlbumForm()
    elif request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album_filtered_list = album_list.filter(title__contains = form.cleaned_data['title'])
            context = {'album_filtered_list' : album_filtered_list, 'form' : form}
            return render(request,'disks/album.html', context)

    album_filtered_list = album_list
    context = {'album_filtered_list' : album_filtered_list, 'form' : form}
    return render(request,'disks/album.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'disks/detail.html', context)
