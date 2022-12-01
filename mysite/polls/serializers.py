
from rest_framework import serializers
from polls.models import Question, Choice


class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['id','question_text','pub_date']

class ChoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields=['id','question','choice_text','votes']

class QuestionChoiceSerializer(serializers.ModelSerializer):
    questions = ChoiceModelSerializer(many=True,read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text','pub_date', 'questions']