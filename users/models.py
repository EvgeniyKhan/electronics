from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = models.CharField(
        max_length=150, unique=True, verbose_name="Имя пользователя"
    )
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=40, verbose_name="Телефон номер", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар", **NULLABLE)
    city = models.CharField(max_length=100, verbose_name="Город", **NULLABLE)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
