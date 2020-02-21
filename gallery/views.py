from django.shortcuts import render
from rest_framework import viewsets
from gallery.models import PhotoAlbum, Photo
from gallery.serializers import PhotoSerializer, PhotoAlbumSerializer
from rest_framework.exceptions import APIException, NotFound


class PhotoViewset(viewsets.ModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self, *args, **kwargs):
        if 'album_id' not in self.kwargs:
            raise APIException('required album_id')
        elif 'album_id' in self.kwargs and not Photo.objects.filter( \
               album_id=self.kwargs['album_id']).exists():
               raise NotFound('Album not found')
        return Photo.objects.filter(album_id=self.kwargs['album_id'])

    def perform_create(self, serializer):
        serializer.save(album_id=int(self.kwargs['album_id']))


class PhotoAlbumViewset(viewsets.ModelViewSet):
    queryset = PhotoAlbum.objects.all()
    serializer_class = PhotoAlbumSerializer
            



