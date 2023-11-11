from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Кастомный класс разрешений.'''

    def has_permission(self, request, view):
        '''Перегружаем метод разрешений уровня запроса.
        Возвращает True (запрос разрешён), только если
        метод в запросе безопасный или юзер дал валидный токен.
        '''
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        '''Перегружаем метод разрешений уровня объекта запроса.
        Возвращает True (доступ к объекту запроса разрешен), если
        автор объекта запроса равен юзеру из запроса.
        '''
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
