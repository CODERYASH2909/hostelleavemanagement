from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return render(request,'login.html')

def student_signup(request):
    return render(request, "student_signup.html")

def student(request):
    return render(request,"student.html")

def rector(request):
    return render(request, "rector.html")

def proctor(request):
    return render(request, "proctor.html")

def hod(request):
    return render(request, "hod.html")

def student_login(request):

    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        if username == "student" and password == "123":

            return redirect('student')   # move forward

        else:
            return render(request,'student_login.html',{'error':'Invalid Login'})

    return render(request,'student_login.html')