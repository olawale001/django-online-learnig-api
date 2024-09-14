from xml.parsers.expat import model
from rest_framework import serializers
from .models import Enrollment

class ErollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'