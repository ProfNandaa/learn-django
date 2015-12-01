from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from polls.models.Question import Question

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.get())
    class Meta:
        model = User
        fields = ('id', 'username', 'questions',)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer