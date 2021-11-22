from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from escola.views import StudentsViewSet, CoursesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', StudentsViewSet, 'Alunos')
router.register('cursos', CoursesViewSet, 'Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
