from django.db import models
from django.contrib.gis.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural='categories'

  def __str__(self):
      return self.name


class Place(models.Model):
  name = models.CharField(max_length=200)
  subhead = models.CharField(max_length=100)
  major_district = models.CharField(max_length=30)
  in_city_area = models.BooleanField(default=False)
  is_world_herritage = models.BooleanField(default=False)
  location=models.PointField(blank=True,null=True)
  description = models.TextField()
  image = models.ImageField(upload_to='places',blank=True,null=True)
  category = models.ManyToManyField(Category,blank=True)

  def __str__(self):
    return self.name

