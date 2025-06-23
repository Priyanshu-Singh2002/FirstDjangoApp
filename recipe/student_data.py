from faker import Faker
from .models import *

fake_obj = Faker()

def create_student_data(n=10)-> None:
    try:
        department_obj = Department.objects.all()
        NOD = len(department_obj)
        for _ in range(n):
            stud_id = f"STU-0{fake_obj.random_int(min=1000, max=9999)}"

            student_id_obj = StudentId.objects.create(student_id = stud_id)

            Stud_data = {
                "department" : department_obj[fake_obj.random_int(0,NOD-1)],
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