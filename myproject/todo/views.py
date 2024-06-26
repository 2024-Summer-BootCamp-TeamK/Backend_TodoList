# APIView import
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import ( PostRequestSerializer,
                            PutRequestSerializer,
                           PutResponseSerializer,
                          GetResponseSerializer)

#데이터 처리
from .models import Todo
from .serializers import TodoSerializer

class TestView(APIView):
    def get(self, request):
        return Response({"message": "hello"}, status=status.HTTP_200_OK)

class TodoListView(APIView):
    @swagger_auto_schema(operation_summary="Todo 전체 조회")
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Todo 생성", request_body=PostRequestSerializer)
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    # todo 조회
    @swagger_auto_schema(operation_summary="단일 Todo 조회",responses= {"200": GetResponseSerializer})
    def get(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    # todo 삭제
    @swagger_auto_schema(operation_summary="단일 Todo 삭제")
    def delete(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response({"error": "Todo Not Found "}, status=status.HTTP_404_NOT_FOUND)

    # todo 수정
    @swagger_auto_schema(operation_summary="단일 Todo 수정", request_body=PutRequestSerializer)
    def put(self, request,id):
        try:
            todo = Todo.objects.get(pk=id)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

