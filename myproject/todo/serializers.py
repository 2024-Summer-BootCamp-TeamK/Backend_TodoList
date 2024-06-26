from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class PostRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100,help_text="todo 제목")
    description = serializers.CharField(max_length=100, help_text="todo 추가설명")
    completed = serializers.BooleanField(read_only=True, help_text="false")
    dueDate_at = serializers.DateField()

# all로 대체 가능
# class PostResponseSerializer(serializers.Serializer):
#     status = serializers.CharField()
#     message = serializers.CharField()

class GetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
class GetResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    completed = serializers.BooleanField(read_only=True)
    dueDate_at = serializers.DateField()

class PutRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100,help_text="todo 제목")
    description = serializers.CharField(max_length=100, help_text="todo 추가설명")
    completed = serializers.BooleanField( help_text="false")
    dueDate_at = serializers.DateField()
class PutResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()