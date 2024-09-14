from urllib import request
from pytz import timezone
from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


    def get_lesson(self, obj):
        request = self.context.get('request')
        user = request.user

        if user.is_authenticated:
            lessons = obj.lessons.filter(release_date_lte=timezone.now())
            return LessonSerializer(lessons, many=True).data
        
        return []