from rest_framework import serializers

from electronics.models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Преобразует объекты модели Product в JSON и обратно, а также выполняет валидацию данных.

    Поля:
        id (int): Уникальный идентификатор продукта.
        name (str): Название продукта.
        model (str): Модель продукта.
        created_date (datetime): Дата создания продукта.
    """

    class Meta:
        model = Product
        fields = ["id", "name", "model", "created_date"]


class NetworkNodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели NetworkNode.

    Преобразует объекты модели NetworkNode в JSON и обратно, а также выполняет валидацию данных.

    Поля:
        id (int): Уникальный идентификатор узла сети.
        name (str): Название узла сети.
        level (int): Уровень узла сети.
        email (str): Электронная почта узла сети.
        country (str): Страна расположения узла сети.
        city (str): Город расположения узла сети.
        street (str): Улица расположения узла сети.
        house_number (str): Номер дома расположения узла сети.
        supplier (str): Поставщик узла сети.
        products (list): Список продуктов, связанных с узлом сети.
        debt (float): Долг узла сети (только для чтения).
        created_at (datetime): Дата и время создания узла сети.

    Поля только для чтения:
        debt (float): Долг узла сети, не подлежит изменению.
    """

    class Meta:
        model = NetworkNode
        fields = [
            "id",
            "name",
            "level",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "products",
            "debt",
            "created_at",
        ]
        read_only_fields = ["debt"]
