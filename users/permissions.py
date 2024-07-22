from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Разрешение для проверки, является ли пользователь администратором (staff).

    Проверяет, имеет ли пользователь статус 'staff', чтобы разрешить доступ к определенным действиям или ресурсам.

    Методы:
        has_permission(request, view): Проверяет, имеет ли пользователь необходимые права доступа.
    """

    def has_permission(self, request, view):
        """
        Проверяет, имеет ли пользователь необходимые права доступа.

        :param request: Объект запроса (HttpRequest), содержащий информацию о текущем пользователе.
        :param view: Объект представления, к которому применяется разрешение.
        :return: bool: True, если пользователь является администратором (staff), иначе False.
        """
        return request.user.is_staff
