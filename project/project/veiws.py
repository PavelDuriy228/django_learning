from django.shortcuts import render

def style_page(request):
    return render(request, 'templates\style_page.html')