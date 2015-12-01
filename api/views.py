from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework import generics
from rest_framework import permissions

from rest_framework import viewsets

from polls.models.Question import Question
from .serializers.question_serializer import QuestionSerializer
from .serializers.user_serializer import UserSerializer
from .permissions import IsOwnerOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
    '''
    This automatically provides a `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    '''
    queryset = Question.get()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
