from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
class sign_up(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required(login_url='/login/')
def index(request):
    todo_list = Todo.objects.order_by('id')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'detail.html', {'todo':todo})

@login_required(login_url='/login/')
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TodoForm()
    return render(request, 'form.html', {'form': form})