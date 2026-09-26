
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('', views.home, name = 'homepage'),
    path('profile/', include('profiles.urls')),
    path('post/', include('posts.urls')),
    path('category/', include('categories.urls')),
]
