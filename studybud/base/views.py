
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

#rooms = [
#   {'id':1, 'name':'Python'},
#    {'id':2, 'name':'Java'},
#    {'id':3, 'name':'C++'},
#]


def home(request): 
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(topic__name__icontains=q)

    topics = Topic.objects.all()

    context = {'rooms': rooms , 'topics' : topics }
    return render(request, 'base/home.html', context )

def room(request,pk):

    #pk parameter will pass the id value in the room 
    #room = None
    #for i in rooms:
    #    if i['id'] == int(pk):
    #        room = i


    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context )

def createroom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context ={'form':form}
    return render(request, 'base/room_form.html', context)

def updateroom(request, pk):
    room = Room.objects.get (id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render (request, 'base/room_form.html' ,context) 

def delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')


    return render(request, 'base/delete.html', {'obj':room})

