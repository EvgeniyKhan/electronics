from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsAdmin
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания нового пользователя.

    Позволяет любому пользователю создавать новые учетные записи пользователей.

    Атрибуты:
        serializer_class (Serializer): Сериализатор для создания нового пользователя.
        queryset (QuerySet): Запрос для получения всех объектов пользователя.
        permission_classes (list): Разрешения, применяемые к этому представлению (разрешает доступ любому пользователю).
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления информации о пользователе.

    Позволяет обновлять данные пользователя только аутентифицированным пользователям или администраторам.

    Атрибуты:
        serializer_class (Serializer): Сериализатор для обновления данных пользователя.
        queryset (QuerySet): Запрос для получения всех объектов пользователя.
        permission_classes (list): Разрешения, применяемые к этому представлению (доступ разрешен аутентифицированным пользователям или администраторам).
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    Представление для удаления пользователя.

    Позволяет удалять учетные записи пользователей только администраторам.

    Атрибуты:
        serializer_class (Serializer): Сериализатор для удаления пользователя.
        queryset (QuerySet): Запрос для получения всех объектов пользователя.
        permission_classes (list): Разрешения, применяемые к этому представлению (доступ разрешен только администраторам).
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdmin]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для получения информации о пользователе.

    Позволяет получать данные о пользователе только аутентифицированным пользователям или администраторам.

    Атрибуты:
        serializer_class (Serializer): Сериализатор для получения данных пользователя.
        queryset (QuerySet): Запрос для получения всех объектов пользователя.
        permission_classes (list): Разрешения, применяемые к этому представлению (доступ разрешен аутентифицированным пользователям или администраторам).
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
