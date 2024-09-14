from rest_framework import serializers
from .models import Question, Quiz, QuizResult, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = '__all__'        