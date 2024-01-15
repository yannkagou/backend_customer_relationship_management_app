from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import LeadViewset

router = DefaultRouter()
router.register('leads', LeadViewset, basename='leads')

urlpatterns = [
    path('', include(router.urls))
]
