from rest_framework import serializers
from .models import Quiz, Question, Choice

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'created_at']
        read_only_fields = ['created_at']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']
    
# --- Nuevos Serializers para Parte 3 ---
class ChoiceDetailSerializer(serializers.ModelSerializer):
    """Para mostrar opciones sin revelar cuál es la correcta"""
    class Meta:
        model = Choice
        fields = ['id', 'text']

class QuestionDetailSerializer(serializers.ModelSerializer):
    """Pregunta con todas sus opciones"""
    choices = ChoiceDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class QuizDetailSerializer(serializers.ModelSerializer):
    """Quiz completo con sus preguntas y opciones"""
    questions = QuestionDetailSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'question_count', 'questions']
    
    def get_question_count(self, obj):
        return obj.questions.count()

class SubmitAnswerSerializer(serializers.Serializer):
    """Para validar las respuestas enviadas"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()

