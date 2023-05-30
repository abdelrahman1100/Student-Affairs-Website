from audioop import reverse
from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student
from .models import GraduatedStudent

# Create your views here.


def add(request):
    return render(request, 'AddStudent.html')


def Add(request):
    template = loader.get_template('AddStudent.html')
    return HttpResponse(template.render({}, request))


def Addrecord(request):
    a = request.POST['id']
    b = request.POST['Name']
    c = request.POST['Date']
    d = request.POST['Gpa']
    m = request.POST['age']
    e = request.POST['Gender']
    g = request.POST['Level']
    h = request.POST['Department']
    i = request.POST['Activation1']
    k = request.POST['Email']
    l = request.POST['MobileNumber']
    Server_App = Student(id=a, name=b, date=c, gpa=d, age=m, gender=e,
                         level=g, dept=h, active=i, email=k, phone_Num=l)
    Server_App.save()
    return HttpResponseRedirect('add')


def chooseproject(request):
    return render(request, 'choos project.html')


def choosedep(request):
    return render(request, 'chooseDept.html', {'students': Student.objects.all()})


def first(request):
    return render(request, 'firstWebPage.html')


def graduated(request):
    return render(request, 'graduatedstudent.html', {'gstudents': GraduatedStudent.objects.all()})


def info(request):
    return render(request, 'infopage (1).html', {'students': Student.objects.all()})


def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('info')
        else:
            return redirect('home')
    return render(request, 'mainpage.html')
