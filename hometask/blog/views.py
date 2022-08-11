from importlib.resources import path
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import student
from django.contrib import messages

# Create your views here.

def index(request):
    return render( request, 'index.html')

def about(request):
    return render( request , 'about.html')

def data(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        student.objects.create(name=name, address=address, phone=phone )
        messages.success(request, 'student added successfully')
        return redirect(data)

 
        #return HttpResponse(name)
    else:
        information = {
            'students' : student.objects.all()
        }
        return render ( request, 'data.html', information)

def contact(request):
    return render( request, 'contact.html')

def delete(request, id):
    student.objects.get(id=id).delete()
    messages.success(request, 'Student deleted successfully')
    return redirect(data)

def update(request, id):
    student.objects.update(id=id).edit()
    messages.success(request, 'Edited successfully')
    return redirect(data)


