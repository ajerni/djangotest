from rest_framework import serializers
from .models import Course

# the serializer handles the convertion of db content from and to json

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'language', 'price')