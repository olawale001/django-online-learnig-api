from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Quiz, QuizResult
from .serializers import QuizSerializer, QuizResultSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

class QuizResultViewSet(viewsets.ModelViewSet):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer    
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]