from .models import Course

def get_course_details(id):
    try:
        course = Course.objects.get(id = id)
        return {
            "name": course.name,
            "code": course.code,
            "description": course.description,
            "credits": course.credits
        }
    except Course.DoesNotExist:
        return {"error":"Course not found"}