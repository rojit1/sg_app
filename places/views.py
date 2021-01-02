from django.shortcuts import render
from .serializers import PlacesSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Place,Category
from rest_framework.filters import SearchFilter,OrderingFilter
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

class PlaceListView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['name','major_district']



class PlaceDetailView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer

class NearPlacesView(ListAPIView):

    model = Place
    serializer_class = PlacesSerializer

    def get_queryset(self):
        longitude = float(self.request.query_params.get('lng'))
        latitude = float(self.request.query_params.get('lat'))
        user_location = Point(longitude, latitude, srid=4326)
        return Place.objects.annotate(distance=Distance('location',user_location)).order_by('distance')[0:3]



    





