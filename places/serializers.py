from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Category, Place

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        files='__all__'


class PlacesSerializer(GeoFeatureModelSerializer):
    # distance = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields='__all__'
        geo_field = 'location'
