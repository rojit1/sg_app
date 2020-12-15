from rest_framework import serializers
from .models import UserProfile
from accounts.serializers import CustomUserSerializer

class UserProfileSerializer(serializers.ModelSerializer):
  user = CustomUserSerializer(read_only=True)
  class Meta:
    model = UserProfile
    fields = '__all__' 