from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def home(request):
    peoples=[
        {'name' : 'Abhijeet','age':21},
        {'name' : 'Amor ', 'age':25},
        {'name' : 'sharat','age': 23},
        {'name' : 'Rasel','age': 24},
        {'name': 'Piyas', 'age': 24},
    ]
    for people in peoples:
        print(people)

    return render(request,"index.html", context={'peoples': peoples})

def contract(request):
    return render(request,"contract.html")

def about(request):
    return render(request,"about.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
