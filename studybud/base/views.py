from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'let us learn python'},
#     {'id': 2, 'name': 'Design With Me'},
#     {'id': 3, 'name': 'Frontend Developers'},
# ]
from django.http import HttpResponse

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)
