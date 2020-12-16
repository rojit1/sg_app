from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Category,Place

admin.site.register(Category)

@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    list_display=('name','location')

