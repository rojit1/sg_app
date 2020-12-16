from rest_framework import serializers
from .models import WishList
from places.serializers import PlacesSerializer


class WishListSerializer(serializers.ModelSerializer):
    place = PlacesSerializer()
    class Meta:
        model = WishList
        fields = ['place']