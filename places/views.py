from django.shortcuts import render
from .serializers import PlacesSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Place,Category
from rest_framework.filters import SearchFilter,OrderingFilter

class PlaceListView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['name','major_district']



class PlaceDetailView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer





