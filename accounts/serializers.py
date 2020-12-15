  
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'firstname', 'lastname', 'password')



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['firstname','lastname','email']