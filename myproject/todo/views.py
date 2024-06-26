from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from .models import Todo
from .serializers import TodoSerializer


class TestView(APIView):
    def get(self, request):
        return Response({"message": "hello"}, status=status.HTTP_200_OK)
class TodoAPI(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        print(queryset)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
