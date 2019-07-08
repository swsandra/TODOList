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

@login_required(login_url='/login/')
def index(request):
    todo_list = Todo.objects.order_by('id')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'index.html', context)

def post_todo(request, new=True, instance=None):
    if request.method == 'POST':
        if new:
            form = TodoForm(request.POST)
        else:
            form = TodoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return None
            # return HttpResponseRedirect('/')
        else:
            for field in form:
                for error in field.errors:
                    err = '{}: {}'.format(field.label,error)
                    messages.error(request,err)
    else:
        if new:
            form = TodoForm()
        else:
            form = TodoForm(instance=instance)
    return form

@login_required(login_url='/login/')
def add(request):
    form = post_todo(request)
    if form is None:
        return HttpResponseRedirect('/')
    return render(request, 'add.html', {'form': form})

@login_required(login_url='/login/')
def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    form = post_todo(request, new=False, instance=todo)
    if form is None:
        return HttpResponseRedirect('/')
    return render(request, 'edit.html', {'todo': todo, 'form': form})

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