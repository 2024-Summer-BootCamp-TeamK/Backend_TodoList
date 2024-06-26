from django.urls import path
from .views import TestView, TodoAPI, TodoDetailAPIView

# 일종의 컨트롤러같이 URL 매핑을 위한 파일
#    path('hello/', TestView.as_view(), name='hello_world'),
#    path('여기에 url경로', (view.py의 클래스명).(그 클래스 속 사용할 함수)(), name = 'url 별칭' )
#    만약 view.py에 class를 안만들고 바로 def만들었다면 view.def명 이렇게 사용


urlpatterns = [
    path('hello/', TestView.as_view(), name='hello_world'),
    path('api/todo/', TodoAPI.as_view(), name='todo_list'), # get, post
    path('api/todo/<int:pk>/', TodoDetailAPIView.as_view(), name='todo_detail'), # update, delete, get
]
