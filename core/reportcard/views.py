from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum

# Create your views here.

def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_id__student_id__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_name__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)
        )

    paginator = Paginator(queryset, 10) 
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'report/students.html', {'queryset' : page_obj})

def see_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    print(total_marks)
    return render(request, 'report/see_marks.html', {'queryset' : queryset, 'total_marks': total_marks})

