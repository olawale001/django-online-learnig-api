from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permission(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]    
        return super().get_permissions() 

    def get_serializer_context(self):
        context = super(CourseViewSet, self).get_serializer_context()   
        context.update({
            'request': self.request
        })
        return context

