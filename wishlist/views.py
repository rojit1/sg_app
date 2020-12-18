from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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
        user_id = request.user.id
        w = WishList.objects.raw(f'select * from wishlist_wishlist where place_id={place.id} and user_id={user_id}')
        if len(w) <= 0:
            WishList.objects.create(place_id=place.id,user_id=user_id)
            return Response({'msg':'Added to wishlist'},status=201)
        else:
            return Response({'msg':'Already in wishlist'},status=403)

    def delete(self,request):
        place = get_object_or_404(Place,pk=request.data['place_id'])
        user_id = request.user.id
        try:
            wishlist =  WishList.objects.raw(f'select * from wishlist_wishlist where place_id={place.id} and user_id={user_id}')[0]
        except IndexError:
            return Response({'msg':'No wishlist available'},status=404)

        if wishlist:
            wishlist.delete()
            return Response({'msg':'Deleted from wishlist'},status=204)
        else:
            return Response({'msg':'No wishlist available'},status=404)

        

