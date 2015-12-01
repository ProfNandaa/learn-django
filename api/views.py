from django.shortcuts import render

# Create your views here.

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework import generics

from polls.models.Question import Question
from .serializers.QuestionSerializer import QuestionSerializer

"""

class QuestionList(APIView):
    '''
    List all questions, or create new ones
    '''
    def get(self, request, format=None):
        questions = Question.get()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class QuestionDetail(APIView):
    '''
    Retrieve, update or delete a questions
    '''
    def get_object(self, pk):
        try:
            question = Question.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
"""

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.get()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.get()
    serializer_class = QuestionSerializer