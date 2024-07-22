from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Преобразует объекты модели User в JSON и обратно, а также выполняет валидацию данных.

    Поля:
        id (int): Уникальный идентификатор пользователя.
        email (str): Электронная почта пользователя.
        phone (str): Номер телефона пользователя.
        avatar (str): URL аватара пользователя.
        city (str): Город пользователя.
    """

    class Meta:
        model = User
        fields = ["id", "email", "phone", "avatar", "city"]
