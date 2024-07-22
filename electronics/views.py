from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления товарами.

    Позволяет выполнять операции CRUD (создание, чтение, обновление, удаление) для объектов товара.

    Атрибуты:
        queryset (QuerySet): Запрос для получения всех объектов товара.
        serializer_class (Serializer): Сериализатор для преобразования объектов товара в JSON и обратно.
        permission_classes (list): Список классов разрешений, применяемых к этому ViewSet.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Сохраняет новый объект товара в базе данных.

        Переопределяет метод perform_create для добавления логики при создании объекта.

        :param serializer: Сериализатор, используемый для создания нового объекта товара.
        """
        serializer.save()


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления узлами сети.

    Позволяет выполнять операции CRUD (создание, чтение, обновление, удаление) для объектов узла сети.

    Атрибуты:
        queryset (QuerySet): Запрос для получения всех объектов узла сети.
        serializer_class (Serializer): Сериализатор для преобразования объектов узла сети в JSON и обратно.
        permission_classes (list): Список классов разрешений, применяемых к этому ViewSet.
        filter_backends (list): Список фильтров, применяемых для поиска и фильтрации объектов.
        filterset_fields (list): Список полей, по которым можно фильтровать объекты.
    """

    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country"]

    def perform_create(self, serializer):
        """
        Сохраняет новый объект узла сети в базе данных.

        Переопределяет метод perform_create для добавления логики при создании объекта.

        :param serializer: Сериализатор, используемый для создания нового объекта узла сети.
        """
        serializer.save()
