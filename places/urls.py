from django.urls import path
from .views import PlaceListView,PlaceDetailView,NearPlacesView

urlpatterns = [
    path('',PlaceListView.as_view()),
    path('<int:pk>/',PlaceDetailView.as_view()),
    path('nearest/',NearPlacesView.as_view())

]