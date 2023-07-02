from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Employee
# Create your views here.
def Login(request):
    if(request.method == 'GET'):
        return render(request,'Login.html',{})
    else:
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = Employee.objects.get(email = email,password=password)
            request.session['email'] = email
            return redirect(Dashboard)
        except:
            msg = 'Plz enter valid details...'
            return render(request,'Login.html',{'msg':msg})
def Signup(request):
    if(request.method == 'GET'):
        return render(request,'Homepage.html',{})
    else:
        ename = request.POST["ename"]
        print(ename)
        email = request.POST['email']
        Birth_date = request.POST['dob']
        gender = request.POST['gender']
        education = request.POST['education']
        password = request.POST['password']
        print(email)
        try:
            email = Employee.objects.get(email = email)
            msg = 'Email id alrady exit...'
            # return render(request,'Homepage.html',{'msg':msg})
            return JsonResponse({'status':'save','msg':msg})
        except:
            data = Employee()
            data.ename = ename
            data.email = email
            data.Birth_date = Birth_date
            data.gender = gender
            data.education = education
            data.password = password
            data.save()
            if('email' in request.session):
                data = Employee.objects.values()
                employee = list(data)
                print('khairnar')
                return JsonResponse({'status':'save','employee':employee})
            else:
                return redirect(Login)
def testing(request):
    id = request.GET['empid']
    data= Employee.objects.filter(id = id).values()
    employee = list(data)
    return JsonResponse({'status':'save','employee':employee})

def Edit(request):
    id = request.POST['empid']
    ename = request.POST["ename"]
    print(ename)
    email = request.POST['email']
    Birth_date = request.POST['dob']
    gender = request.POST['gender']
    education = request.POST['education']
    password = request.POST['password']
    data = Employee.objects.get(id = id)
    data.ename = ename
    data.email = email
    data.Birth_date = Birth_date
    data.gender = gender
    data.education = education
    data.password = password
    data.save()
    data = Employee.objects.values()
    employee = list(data)
    print('khairnar')
    return JsonResponse({'status':'save','employee':employee})

def Remove(request):
    id = request.POST['empid']
    print('ID :',id)
    emp = Employee.objects.get(id=id)
    emp.delete()
    data = Employee.objects.values()
    employee = list(data)
    return JsonResponse({'status':'save','employee':employee})

def Logout(request):
    request.session.clear()
    return redirect(Signup)

def Dashboard(request):
    if('email' in request.session):
        data = Employee.objects.all()
        return render(request,'Dashboard.html',{"data":data})
    return redirect(Login)

def save(request):
    print('abc')
    if(request.method == 'POST'):
        data = Employee.objects.values()
        std = list(data)
        print('khairnar')
        return JsonResponse({'status':'save','std':std})
        
