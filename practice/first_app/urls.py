from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:idMeal>/', views.meal_page, name='meal_page'),
]