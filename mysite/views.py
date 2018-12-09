from django.shortcuts import render
from .models import blog
from mysite import models
# Create your views here.
def blog(request):
    bl = models.blog.objects.all()
    return render(request,'blog.html',{'bl':bl})
