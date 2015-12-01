from django.conf.urls import include, url
# from rest_framework import routers

# from .serializers.user_serializer import UserViewSet

import views

# router = routers.DefaultRouter()
# router.register(r'^users', UserViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^question/$', views.QuestionList.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
