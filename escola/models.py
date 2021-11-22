from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices

class Student(models.Model):
    name= models.CharField(max_length=30, blank=False, null=False)
    rg= models.CharField(max_length=9, blank=False, null=False)
    cpf= models.CharField(max_length=11)
    birth_date= models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    NIVEL = (
        ('B','Basico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )

    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description

class Subscription(models.Model):
    PERIOD = {
        ('M', 'Matutino'),
        ('V', 'Verspertino'),
        ('N', 'Noturno')
    }

    period = models.CharField(max_length=1, null= False, blank=False, choices=PERIOD, default='N')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)