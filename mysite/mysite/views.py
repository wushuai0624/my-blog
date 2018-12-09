from django.shortcuts import render_to_response
from blog.models import Blog,BlogType


def home(request):
    context={
    }
    dates = []
    read_nums = []
    blogs = Blog.objects.all()
    for blog in blogs:
        date=blog.created_time.strftime('%m/%d')
        date_lastup = blog.last_updated_time.strftime('%m/%d')
        if date not in dates:
           dates.append(date)
           read_nums.append(blog.read_num)
        elif date_lastup not in dates:

            dates.append(date_lastup)
            read_nums.append(blog.read_num)
        else:
            if date_lastup !=date:
                index = dates.index(date)
                read_nums[index]+=blog.read_num
    dates.sort()
    read_nums.sort()
    context['dates'] = dates
    context['read_num'] = read_nums
    print('检测 数据',dates, read_nums)
    return render_to_response('home.html', context)



def login(request):
    context = {}
    return render_to_response('login.html',context)