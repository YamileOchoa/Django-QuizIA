from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz
from .serializers import QuizSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': '🧠 Welcome to Quiz.AI API',
        'version': 'v1.0',
        'description': 'Intelligent Quiz Management System',
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
        }
    })

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer