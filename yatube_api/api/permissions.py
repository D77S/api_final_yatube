from rest_framework import permissions


class MethodIsSafeOrUserIsAuthor(permissions.BasePermission):
    '''Кастомный класс разрешений.'''

    def has_permission(self, request, view):
        '''Перегружаем метод разрешений уровня запроса.
        Возвращает True (запрос разрешён), только если
        метод в запросе безопасный или юзер идентифицирован.
        '''
        # Замечание ревьюера:
        # Если класс назвали IsOwnerOrReadOnly, то он не должен
        # проверять is_authenticated, это противоречит его названию. 
        # Надо либо менять название, либо дополнительно использовать
        # стандартный IsAuthenticated в контроллере.
        # Устранено: переназвал мой пермишен.
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        '''Перегружаем метод разрешений уровня объекта запроса.
        Возвращает True (доступ к объекту запроса разрешен), только если
        метод в запросе безопасный или юзер - автор объекта запроса.
        '''
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
