from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from escola.views import StudentsViewSet, CoursesViewSet, SubscriptionViewSet, StudentCourses, CourseStudents
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', StudentsViewSet, 'Alunos')
router.register('cursos', CoursesViewSet, 'Cursos')
router.register('matriculas', SubscriptionViewSet, 'Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/',StudentCourses.as_view()),
    path('cursos/<int:pk>/matriculas/',CourseStudents.as_view())
]
