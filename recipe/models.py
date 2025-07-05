from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='recipes', null=True, blank=True)
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe_images/')
    recipe_view_count = models.IntegerField(default=0)

class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

    class Meta:
        ordering = ['department_name']
    

class StudentId(models.Model):
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.student_id
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

    class Meta:
        ordering = ['subject_name']


class Student(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name='department_students')
    student_id = models.OneToOneField(StudentId, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_phone = models.CharField(max_length=15, unique=True)
    student_age = models.PositiveIntegerField()
    student_address = models.TextField()


    def __str__(self):
        return f"{self.student_name} ({self.student_id})"
    

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'


class StudentSubjectMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    mark = models.PositiveIntegerField()
    report = models.ForeignKey('StudentReportCard', on_delete=models.CASCADE, related_name='subject_marks', null=True, blank=True)

    def __str__(self):
        return f'{self.student.student_name} - {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student', 'subject']
        ordering = ['student__student_name', 'subject__subject_name']


class StudentReportCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='report_card')  # Ensures one report per student
    rank = models.PositiveIntegerField(null=True, blank=True)
    total_marks = models.PositiveIntegerField()
    result = models.CharField(max_length=4, null=False, default='pass/fail')
    date_of_generating = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.student_name} - {self.rank}'
    
    class Meta:
        ordering = ['student__student_name']
