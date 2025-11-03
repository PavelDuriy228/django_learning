import requests
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
# Create your views here.

def  home_page(request: HttpRequest):
    return render(
        request, 
        'pet_proj_templates\learn_page.html'
    )

def get_submit_data(request, id):
    url = f"https://api.saidbamu.beget.tech/submitData/{id}/"

    # Вообщем хз видимо сайт не работает ошибка 502 
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # выбросит ошибку, если код != 200
        data = response.json()       # преобразуем JSON-ответ
        return JsonResponse(data, safe=False, status=200)
    except requests.exceptions.HTTPError as e:
        # Ошибки сервера (404, 405 и т.д.)
        return JsonResponse({"error": str(e)}, status=response.status_code)
    except Exception as e:
        # Прочие ошибки (сетевые, кодирование и т.п.)
        return JsonResponse({"error": str(e)}, status=500)