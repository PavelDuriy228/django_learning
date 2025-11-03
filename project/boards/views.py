from django.shortcuts import render
from .models import Bulletin, News

def board_main(request):
    return render(request, 'board/index.html')

def news_page(request):
    news_list = News.objects.order_by("-created_at")
    return render(request, 'board/news.html', {'news_list':news_list})

def bullet_page(request):
    bullet_list = Bulletin.objects.order_by("-created_at")
    return render(request, 'board/bullet.html', {'bullet_list':bullet_list})

def resp_page(request):
    return render(request, 'board/resp.html')
