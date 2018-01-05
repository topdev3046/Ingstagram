"""from django.shortcuts import render"""
from rest_framework.views import APIViews
from rest_framework.response import Response
from . import models, serializers


class ListAllImages(APIViews):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)
