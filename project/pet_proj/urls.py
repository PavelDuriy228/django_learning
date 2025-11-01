from django.urls import path
from . import views

app_name= "pet_proj"

urlpatterns = [
    path('', views.home_page ,name='home_page'),
    path('api/<int:id>/', views.get_submit_data, name="get_submit_data")
]
