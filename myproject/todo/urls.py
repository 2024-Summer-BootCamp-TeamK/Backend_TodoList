from django.urls import path
from .views import TestView, TodoListView, TodoDetailView

urlpatterns = [
    path('hello/', TestView.as_view(), name='hello_world'),
    path('api/todo', TodoListView.as_view(), name='todo_list'),
    path('api/todo/<int:id>', TodoDetailView.as_view(), name='todo_detail'),
]
