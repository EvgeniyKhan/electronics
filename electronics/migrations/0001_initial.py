# Generated by Django 5.0.7 on 2024-07-22 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Название")),
                ("model", models.CharField(max_length=300, verbose_name="Модель")),
                (
                    "created_date",
                    models.DateField(verbose_name="Дата выхода продукта на рынок"),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="NetworkNode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Название")),
                (
                    "level",
                    models.PositiveIntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Розничная сеть"),
                            (2, "Индивидуальный предприниматель "),
                        ],
                        verbose_name="Уровень",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Почта"
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Улица"
                    ),
                ),
                (
                    "house_number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Номер дома"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="electronics.networknode",
                        verbose_name="Поставщик",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        default=None, to="electronics.product", verbose_name="Продукты"
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент сети",
                "verbose_name_plural": "Элементы сети",
            },
        ),
    ]