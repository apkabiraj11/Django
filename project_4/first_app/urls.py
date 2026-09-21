from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('form/', views.submit_form, name='submit_form'),
    path('DjangoForm/', views.PasswordValidation, name='DjangoForm')
]
