from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def  home_page(requests: HttpRequest):
    return render(
        requests, 
        'pet_proj\\templates\learn_page.html'
    )

