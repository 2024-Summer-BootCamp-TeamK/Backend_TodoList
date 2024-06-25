from django.urls import path
from .views import ToDoAPIView, ToDoManageView

urlpatterns = [
    path('todos/', ToDoAPIView.as_view(), name='todo_list'),
    path('todos/<int:id>', ToDoManageView.as_view(), name='todo_list_update'),
]
