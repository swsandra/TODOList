from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada, por favor inicie sesión.')
        else:
            for field in form:
                for error in field.errors:
                    err = '{}: {}'.format(field.label,error)
                    messages.error(request,err)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 messages.error(request,'El usuario no existe.')
#         else:
#             messages.error(request,'Usuario o contraseña incorrecta.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def index(request):
    todo_list = Todo.objects.order_by('id')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            for field in form:
                for error in field.errors:
                    err = '{}: {}'.format(field.label,error)
                    messages.error(request,err)
    else:
        form = TodoForm()
    return render(request, 'add.html', {'form': form})

@login_required(login_url='/login/')
def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'detail.html', {'todo': todo})

@login_required(login_url='/login/')
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    messages.success(request, 'Tarea eliminada.')
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def complete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.status = 1
    todo.save()
    return HttpResponseRedirect('/')