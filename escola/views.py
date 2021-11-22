from django.db.models.query import QuerySet
from rest_framework import serializers, viewsets, generics
from rest_framework import authentication
from rest_framework import permissions
from escola.models import Student, Course, Subscription
from escola.serializer import StudentSerializer, CourseSerializer, SubscriptionSerializer, StudentCoursesSerializer, CourseStudentsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    # exibe todos os alunos e alunas
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    # exibe todos os alunos e alunas
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    # exibe todos os alunos e alunas
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class StudentCourses(generics.ListAPIView):
    #exibe os cursos de um aluno ou aluna
    def get_queryset(self):
        queryset = Subscription.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = StudentCoursesSerializer

class CourseStudents(generics.ListAPIView):
    #exibe os alunos de um curso
    def get_queryset(self):
        queryset = Subscription.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = CourseStudentsSerializer
