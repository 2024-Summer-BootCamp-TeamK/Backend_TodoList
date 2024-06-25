from django.urls import path
from .views import ToDoAPIView

urlpatterns = [
    path('todos/', ToDoAPIView.as_view(), name='todo_list'),
]
