from django.urls import path

from . import views

app_name = 'disks'
urlpatterns = [
    # ex: /disks/
    path('', views.album, name='album'),

    # ex: /disks/5/
    path('<int:album_id>/', views.detail, name='detail'),
]