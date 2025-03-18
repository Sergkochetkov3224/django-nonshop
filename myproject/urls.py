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
from django.contrib.auth.models import User

def create_superuser(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
        return HttpResponse("Суперюзер создан! Логин: sergkochetkov | Пароль: Sergey2005")
    return HttpResponse("Суперюзер уже существует!")

urlpatterns.append(path("create-admin/", create_superuser))
from django.core.management import call_command

def migrate(request):
    call_command("migrate")
    return HttpResponse("Миграции успешно выполнены!")

urlpatterns.append(path("migrate/", migrate))
