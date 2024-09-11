# models.py (in the student app)

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    section = models.CharField(max_length=5)
    branch = models.CharField(max_length=100)
    technical_skills = models.CharField(max_length=200)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    mobile = models.CharField(max_length=10)
    joining_year = models.IntegerField()

    def __str__(self):
        return self.name

