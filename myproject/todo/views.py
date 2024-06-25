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