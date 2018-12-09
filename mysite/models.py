from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    text = models.TextField()
    time = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    class Meta:
        verbose_name = u'博客'
        verbose_name_plural=verbose_name