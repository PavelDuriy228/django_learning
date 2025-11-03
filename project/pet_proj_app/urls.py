from django.urls import path
from . import views

app_name= "pet_proj_app"

urlpatterns = [
    path('', views.test_page ,name='home_page'),
    path('api/<int:id>/', views.get_submit_data, name="get_submit_data"),
    path('test/', views.test_page, name = 'test_page')
]
