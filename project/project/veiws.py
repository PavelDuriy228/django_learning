from django.shortcuts import render

def style_page(request):
    return render(request, 'style_page.html')