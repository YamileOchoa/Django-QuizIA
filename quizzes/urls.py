from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, api_root

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]