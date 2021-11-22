from rest_framework import viewsets
from escola.models import Student, Course
from escola.serializer import StudentSerializer, CourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    # exibe todos os alunos e alunas
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    # exibe todos os alunos e alunas
    queryset = Course.objects.all()
    serializer_class = CourseSerializer