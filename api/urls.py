from django.conf.urls import include, url
from rest_framework import routers

from .serializers import UserSerializer

router = routers.DefaultRouter()
router.register(r'^users', UserSerializer.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
