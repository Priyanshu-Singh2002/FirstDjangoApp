from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .recipe_db import get_recipes
from django.core.paginator import Paginator
from .models import *
from django.db.models import Q

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("add_recipe"))
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect(reverse("login_page"))


def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        # save data to database
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        return redirect(reverse("login_page"))
    else:
        return render(request, "register.html")


# Create your views here.
@login_required(login_url="/login/")
def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("recipe_name")
        description = data.get("recipe_description")
        image = request.FILES.get("recipe_image")
        user = request.user
        # save data to database
        Recipe.objects.create(
            recipe_name=name, recipe_description=description, recipe_image=image, user=user
        )
        return redirect(reverse("add_recipe"))
    else:
        # recipes = Recipe.objects.all()
        recipes = get_recipes(request.user.id)
        search_key = request.GET.get("search")
        if search_key:
            recipes = recipes.filter(recipe_name__icontains=search_key)
        return render(request, "recipe_front.html", context={"recipes": recipes})
    

@login_required(login_url="/login/")
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect(reverse("add_recipe"))


@login_required(login_url="/login/")
def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get("recipe_name")
        description = data.get("recipe_description")
        # update recipe
        recipe.recipe_name = name
        recipe.recipe_description = description

        if "recipe_image" in request.FILES:
            recipe.recipe_image = request.FILES.get("recipe_image")
        else:
            recipe.recipe_image = recipe.recipe_image

        recipe.save()
        return redirect(reverse("add_recipe"))
    return render(request, "update_recipe.html", context={"recipe": recipe})
    

def get_student(request):
    students = Student.objects.all()

    if request.GET.get("search"):
        search_key = request.GET.get("search")
        students = students.filter(
            Q(department__department_name__icontains=search_key)|
            Q(student_name__icontains=search_key)|
            Q(student_id__student_id__icontains=search_key)|
            Q(student_email__icontains=search_key)|
            Q(student_phone__icontains=search_key)|
            Q(student_age__icontains=search_key)|
            Q(student_address__icontains=search_key)   
        )

    paginator = Paginator(students,10)
    page_num = request.GET.get('page', 1)
    data_page = paginator.get_page(page_num)
    return render(request,'report/student.html', context={"students": data_page})


def get_student_report(request,id):
    report = StudentReportCard.objects.filter(student__student_id__student_id = id).first()

    if not report:
        return render(request, 'report/student_report.html', {'error': 'No report found'})
    marks = StudentSubjectMark.objects.filter(report = report)
    
    context = {
        'report':report,
        'student':report.student,
        'subj_marks' : marks
    }
    return render(request,'report/student_report.html',context)
