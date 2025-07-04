from faker import Faker
import random
from .models import *
from django.db.models import Sum

fake_obj = Faker()


def create_Stud_subj_marks() -> None:
    try:
        Student_obj = Student.objects.all()
        Subject_obj = Subject.objects.all()
        TP = len(Student_obj)
        TS = len(Subject_obj)
        if TP == 0 or TS == 0:
            raise ValueError("No students or subjects available to create marks.")
        for i in range(TP):
            for j in range(TS):
                StudentSubjectMark.objects.create(
                    student = Student_obj[i],
                    subject = Subject_obj[j],
                    mark = random.randint(0, 100)
                )
    except Exception as e:
        print(f"Error creating student subject marks: {e}")


def create_student_data(n=10)-> None:
    try:
        department_obj = Department.objects.all()
        NOD = len(department_obj)
        for _ in range(n):
            stud_id = f"STU-0{random.randint(1000, 9999)}"

            student_id_obj = StudentId.objects.create(student_id = stud_id)

            Stud_data = {
                "department" : department_obj[random.randint(0,NOD-1)],
                "student_id" : student_id_obj,
                "student_name" : fake_obj.name(),
                "student_email" : fake_obj.email(),
                "student_phone" : '+91-' + fake_obj.numerify(text='##########'),
                "student_age" : fake_obj.random_int(min=18, max=28),
                "student_address" : fake_obj.address(),
            }

            Student.objects.create(**Stud_data)
    
    except Exception as e:
        print(f"Error creating student data: {e}")


def generate_rank_student() -> None:
    Stud_Det = Student.objects.annotate(total_marks = Sum('marks__mark')).order_by('-total_marks')
    i = 1
    for stud in Stud_Det:
        StudentReportCard.objects.create(
            student = stud,
            rank = i,
            total_marks = stud.total_marks
        )
        i = i + 1

    
def set_report():
    report = StudentReportCard.objects.all()
    marks = StudentSubjectMark.objects.all()
    n = 1

    for r in report:
        n = 1
        for m in marks:
            if (m.student == r.student) and (n <= 4):
                m.report = r
                m.save()
                n = n + 1
                continue
            if(n > 4):
                break



# student_marks = StudentSubjectMark.objects.filter(student=report.student, report__isnull=True)[:4]
