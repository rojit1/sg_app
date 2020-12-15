from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib.auth import get_user_model
from .models import UserProfile
User = get_user_model()

class UserProfileView(APIView):

  parser_classes = MultiPartParser, FormParser

  def get(self,request,*args,**kwargs):
    try:
      userprofile = UserProfile.objects.get(user=request.user)
      serializer = UserProfileSerializer(instance=userprofile)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
      user = {
        'firstname':request.user.firstname,
        'lastname':request.user.lastname,
        'email':request.user.email,
      }
      return Response(user,status=status.HTTP_200_OK)

    


      

    


