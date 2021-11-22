from django.contrib import admin
from escola.models import Student, Course, Subscription

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'nivel')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Course, Courses)

class Subscriptions(admin.ModelAdmin):
    list_display = ('id', 'period', 'student', 'course')
    list_display_links = ('id', 'course', 'student')
    search_fields = ('course','student',)
    list_per_page = 20

admin.site.register(Subscription, Subscriptions)