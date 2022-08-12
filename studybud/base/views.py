from django.shortcuts import render
from .models import Room

# Create your views here.

#rooms = [
#   {'id':1, 'name':'Python'},
#    {'id':2, 'name':'Java'},
#    {'id':3, 'name':'C++'},
#]


def home(request):
    
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context )

def room(request, pk):

    #pk parameter will pass the id value in the room 
    #room = None
    #for i in rooms:
    #    if i['id'] == int(pk):
    #        room = i


    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context )