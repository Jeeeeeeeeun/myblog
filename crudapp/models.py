from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add = True) # 만든 날짜, 시각 자동 저장
    updated_at = models.DateTimeField(auto_now = True) # 수정 날짜, 시각 자동 저장

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]

class Scrap(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
