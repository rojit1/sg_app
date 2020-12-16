from django.shortcuts import render
from .serializers import PlacesSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Place,Category

class PlaceListView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer


class PlaceDetailView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer





