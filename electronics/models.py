from django.db import models

from config.settings import NULLABLE


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    model = models.CharField(max_length=300, verbose_name="Модель")
    created_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель "),
    ]
    name = models.CharField(max_length=300, verbose_name="Название")
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, verbose_name="Уровень")
    email = models.EmailField(unique=True, verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город", **NULLABLE)
    street = models.CharField(max_length=100, verbose_name="Улица", **NULLABLE)
    house_number = models.CharField(
        max_length=10, verbose_name="Номер дома", **NULLABLE
    )
    supplier = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Поставщик", **NULLABLE
    )
    products = models.ManyToManyField("Product", default=None, verbose_name="Продукты")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Элемент сети"
        verbose_name_plural = "Элементы сети"
