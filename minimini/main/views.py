from django.shortcuts import render

from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    stud=Student.objects.all()
    return render(request,"home.html",{"student":stud})