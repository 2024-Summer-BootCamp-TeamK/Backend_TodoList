from django.db import models

# Create your models here.
# 약간 리포지토리느낌

class Todo(models.Model):
    title = models.CharField(max_length=200)               # 할 일 제목
    content = models.TextField()                           # 할 일 내용
    create_date = models.DateTimeField(auto_now_add=True)  # 작성 시간
    deadline = models.DateTimeField()                      # 마감 기한
    done = models.BooleanField(default=False)              # 완료 여부
    def __str__(self):
        return self.title
