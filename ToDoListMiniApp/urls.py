from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('signup/', views.sign_up, name='signup'),
    path('add/', views.add_todo, name='form'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]