from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ssh_id>/', views.ssh_connect, name='ssh_connect'),
]
