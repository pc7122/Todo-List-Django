from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Tasks


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if username and email and password and password == cpassword:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('/login/')

    return render(request, 'register.html')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def taskList(request):
    tasks = Tasks.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'taskslist.html', context)


@login_required(login_url='/login/')
@require_http_methods(['POST'])
def add_task(request):
    title = request.POST.get('title', '')
    if title:
        user = request.user
        task = Tasks(user=user, title=title)
        task.save()
    return redirect('/')


@login_required(login_url='/login/')
def update_task(request, id: int):
    task = Tasks.objects.get(id=id)
    task.complete = not task.complete
    task.save()
    return redirect('/')


@login_required(login_url='/login/')
def delete_task(request, id: int):
    task = Tasks.objects.get(id=id)
    task.delete()
    return redirect('/')
