from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz, Question, Choice  # ← ahora incluye Question y Choice
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer  # ← incluye los nuevos serializers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': '🧠 Welcome to Quiz.AI API',
        'version': 'v1.0',
        'description': 'Intelligent Quiz Management System',
        'workflow': [
            '1️⃣ Create a quiz (POST /quizzes/)',
            '2️⃣ Add questions (POST /questions/)',
            '3️⃣ Add choices (POST /choices/)',
            '4️⃣ View complete quiz (GET /quizzes/{id}/)',
            '5️⃣ Submit answers (POST /quizzes/{id}/submit/) - Coming in Part 3!'
        ],
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
            'questions': reverse('question-list', request=request, format=format),
            'choices': reverse('choice-list', request=request, format=format),
        }
    })

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer