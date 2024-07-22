from django.contrib import admin

from electronics.models import NetworkNode, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "created_date")
    search_fields = ("name", "model")


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "supplier",
        "debt",
        "created_at",
    )
    search_fields = ("name", "email", "country", "city")
    list_filter = ("city",)
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        """
        Очистить задолженность перед поставщиком для выбранных объектов.

        Параметры:
        - request: Объект запроса Django.
        - queryset: Критерии для выбора объектов для действия.
        """
        queryset.update(debt=0.00)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
