from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)


class SubjectMarksTable(admin.ModelAdmin):
    list_display = ['student', 'subject', 'mark']


admin.site.register(StudentSubjectMark,SubjectMarksTable)


class StudentReportFormat(admin.ModelAdmin):
    ordering = ['-total_marks']
    list_display = ['student','rank','total_marks','date_of_generating']

    

admin.site.register(StudentReportCard,StudentReportFormat)