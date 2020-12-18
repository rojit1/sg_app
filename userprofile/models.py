from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
  country = models.CharField(max_length=50,null=True)
  address = models.CharField(max_length=100,null=True)
  dob = models.DateField(null=True)
  image = models.ImageField(upload_to='user_images',null=True,blank=True)
  user = models.OneToOneField(User,on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user.firstname} {self.user.lastname}'