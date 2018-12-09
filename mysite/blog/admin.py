from django.contrib import admin
from .models import BlogType, Blog

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmain(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'created_time','read_num', 'last_updated_time')