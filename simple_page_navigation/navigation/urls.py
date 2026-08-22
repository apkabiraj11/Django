from django.urls import path
from . import views
urlpatterns = [
    path('About/', views.About),
    path('Contact/', views.Contact),
]
