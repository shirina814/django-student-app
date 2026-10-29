
# Create your views here.

from django.shortcuts import render
from .models import Student


def home(request):
    if not Student.objects.exists():
        Student.objects.bulk_create([
            Student(name="Aisha", course="CSE"),
            Student(name="Rahul", course="ECE"),
            Student(name="Priya", course="IT"),
        ])

    students = Student.objects.all()
    return render(request, "students/index.html", {
        "students": students
    })