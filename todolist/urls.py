from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('task', views.task, name = 'task'),
    path('detail/<str:pick>', views.detail, name='detail'),
]