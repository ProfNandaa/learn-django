from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

import views

router = DefaultRouter()
router.register(r'^users', views.UserViewSet)
router.register(r'^questions', views.QuestionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
