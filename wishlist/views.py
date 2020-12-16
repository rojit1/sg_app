from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WishList
from .serializers import WishListSerializer
from django.shortcuts import get_object_or_404
from places.models import Place

class WishListView(APIView):
    def get(self,request):
        q = WishList.objects.filter(user_id = request.user.id)
        serializer = WishListSerializer(instance=q,many=True)
        return Response(serializer.data,status=200)


    def post(self,request):
        place = get_object_or_404(Place,pk=request.data['place_id'])
        WishList.objects.get(place=place) & WishList.objects.get(user=request.user)
        # WishList.objects.create(user=request.user,place=place)
        return Response({'msg':'Added to wishlist'},status=201)

