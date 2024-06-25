from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import ToDo
from .serializers import ToDoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ToDoAPIView(APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ToDoSerializer,
        responses={
            201: openapi.Response('Created', ToDoSerializer),
            400: 'Bad Request'
        }
    )
    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoManageView(APIView):
    @swagger_auto_schema(
        request_body=ToDoSerializer,
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, description="ID of the ToDo item to update",
                              type=openapi.TYPE_INTEGER)
        ],
        responses={
            200: openapi.Response('OK', ToDoSerializer),
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def put(self, request, id):
        todo = get_object_or_404(ToDo, pk=id)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, description="ID of the ToDo item to delete",
                              type=openapi.TYPE_INTEGER)
        ],
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request, id):
        todo = get_object_or_404(ToDo, pk=id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)