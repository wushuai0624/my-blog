from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    read_num = models.IntegerField(default=0)

    def __str__(self):
        return "<Blog: %s>" % self.title
    class Meta:# 设置排序信息 按照时间 倒续 最新创建的 先看到
        ordering = ['-created_time']