from django.contrib import admin
from django.urls import path, include
from restaurant import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path("", views.index, name="home"),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
]

