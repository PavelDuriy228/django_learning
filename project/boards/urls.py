from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_main, name='board_main'),
    path('news/', views.news_page, name='news'),
    path('bullet/', views.bullet_page, name='bullet'),
    path('resp/', views.resp_page, name='resp'),
]
