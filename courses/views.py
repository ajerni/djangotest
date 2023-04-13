from rest_framework import viewsets
from .models import Course, Geburtstag
from .serializers import CourseSerializer, GeburtstagSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GeburtstagView(viewsets.ModelViewSet):
    queryset = Geburtstag.objects.all()
    serializer_class = GeburtstagSerializer

    def get_queryset(self):
        queryset = Geburtstag.objects.all()
        vorname = self.request.query_params.get('vorname', None)
        nachname = self.request.query_params.get('nachname', None)
        if vorname is not None:
            queryset = queryset.filter(vorname=vorname)
        if nachname is not None:
            queryset = queryset.filter(nachname=nachname)
        return queryset