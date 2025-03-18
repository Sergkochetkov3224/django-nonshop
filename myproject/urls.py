from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет, Пупсик! Сайт работает! 🚀")

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  # Добавляем главную страницу
]
