from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import activate_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activate/<str:uid>/<str:token>/',activate_account),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/profile/', include('userprofile.urls')),
    path('api/v1/places/', include('places.urls')),
    path('api/v1/wishlist/', include('wishlist.urls')),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

