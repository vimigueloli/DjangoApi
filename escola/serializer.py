from rest_framework import serializers
from escola.models import Student, Course, Subscription

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = []

class StudentCoursesSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Subscription
        exclude = ['student']
    def get_period(self,obj):
        return obj.get_period_display()

class CourseStudentsSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    rg = serializers.ReadOnlyField(source='student.rg')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Subscription
        fields = ['student', 'rg', 'period']
    def get_period(self,obj):
        return obj.get_period_display()