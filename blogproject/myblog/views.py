# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request, 'myblog/index.html', context={
#                       'title': '我的博客首页', 
#                       'welcome': '欢迎访问我的博客首页'
#                   })
from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'myblog/index.html', context={'post_list': post_list})