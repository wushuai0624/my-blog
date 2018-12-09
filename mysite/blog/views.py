from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator # 导入分页核心类
from .models import Blog, BlogType
# Create your views here.

def blog_list(request):
    '''分页博客列表'''
    blogs_all_list = Blog.objects.all()
    paginator=Paginator(blogs_all_list,3) # 每 5篇进行一次分页
    page_number = request.GET.get('page', 1)  # 获取页码参数
    page_of_blogs=paginator.get_page(page_number)                 # 使用django自带的 页码处理函数


    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    # context['blogs_count'] = Blog.objects.all().count() # 这个方法也可以传过去一个变量 统计数量
    return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    if not request.COOKIES.get('blog_%s_read' %blog_pk):# 在赫里取出COOKies 判断是否有cookie
        blog.read_num+=1
        blog.save()

    context['previous_blog']=Blog.objects.filter(created_time__gt=blog.created_time).last()# 大于当前博客时间 的最后一条
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog']=blog
    response = render_to_response('blog_detail.html', context)
    # 设置cookie  max_age ：多少秒之后过期, expires设置日期  如果不设置失效时间 cookie会等到 浏览器关闭自己失效
    response.set_cookie('blog_%s_read' %blog_pk,'true')
    return response


def blogs_with_type(request, blog_type_pk):


    context ={}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blog_type'] = blog_type
    # 过滤博客类型
    blogs= Blog.objects.filter(blog_type=blog_type)
    # 分页
    paginator = Paginator(blogs, 3)  # 每 5篇进行一次分页
    page_number = request.GET.get('page', 1)  # 获取页码参数
    page_of_blogs = paginator.get_page(page_number)  # 使用django自带的 页码处理函数
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog_with_type.html', context)

# 注册
def regist():
    pass

