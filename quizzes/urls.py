from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, api_root
from . import views

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)    # ← nueva ruta
router.register(r'choices', ChoiceViewSet)        # ← nueva ruta

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    path('', views.quiz_form_view, name='quiz_form')
]