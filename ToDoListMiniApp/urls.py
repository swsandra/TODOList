from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit_<int:todo_id>/', views.edit, name='edit'),
    path('delete_<int:todo_id>/', views.delete, name='delete'),
    path('complete_<int:todo_id>/', views.complete, name='complete'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]