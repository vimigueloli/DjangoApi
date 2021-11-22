from django.db import models

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