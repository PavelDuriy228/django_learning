from django.shortcuts import render

def board_main(request):
    return render(request, 'board/index.html')

def news_page(request):
    return render(request, 'board/news.html')

def bullet_page(request):
    return render(request, 'board/bullet.html')

def resp_page(request):
    return render(request, 'board/resp.html')
