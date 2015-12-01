from rest_framework import serializers

from polls.models.Question import Question

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date','owner',)