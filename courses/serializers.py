from rest_framework import serializers
from .models import Course
from .models import Geburtstag

# the serializer handles the convertion of db content from and to json

#class CourseSerializer(serializers.ModelSerializer):
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')

class GeburtstagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geburtstag
        fields = ('__all__')
        extra_kwargs = {'rufname': {'required': False}} # write-only etc.
        