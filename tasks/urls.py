from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='tasks'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_task, name='add'),
    path('update/<int:id>/', views.update_task, name='update'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
]
