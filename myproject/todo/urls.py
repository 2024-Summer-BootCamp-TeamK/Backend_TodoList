from django.urls import path
from .views import ToDoAPIView, ToDoUpdateView

urlpatterns = [
    path('todos/', ToDoAPIView.as_view(), name='todo_list_create'),
    path('todos/<int:id>', ToDoUpdateView.as_view(), name='todo_list_update'),
]
