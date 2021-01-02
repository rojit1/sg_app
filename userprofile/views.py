from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib.auth import get_user_model
from .models import UserProfile
User = get_user_model()

class UserProfileView(APIView):

  # parser_classes = MultiPartParser, FormParser

  def get(self,request,*args,**kwargs):
    try:
      userprofile = UserProfile.objects.get(user=request.user)
      serializer = UserProfileSerializer(instance=userprofile)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
      return Response({'msg':'ok'},status=status.HTTP_304_NOT_MODIFIED)

  def post(self,request,format=None):
    data = request.data
    data['user'] = request.user
    try:
      UserProfile.objects.get(user=request.user)
    except Exception:
      UserProfile.objects.create(**data)
    return Response({'msg':'ok'})

  def put(self,request):
    user_profile = request.user.userprofile
    user_profile.country =  request.data['country']
    user_profile.address =  request.data['address']
    user_profile.save()
    return Response({'msg':"updated"})




    


      

    


