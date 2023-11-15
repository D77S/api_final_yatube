from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')
router_v1.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    # Замечание: если используется djoser, то подключаются
    # только урлы для токена/
    #  Подключение к маршрутам include('djoser.urls') не допустимо.
    # Этих урлов нет в спеке.
    #
    #  Урлов djozer'а базовых, на регистрацию нового юзера,
    #  в спецификации нет - придется убрать их из паттернов.
    #  Хотя с ними было очень удобно регать юзеров через поцман.
    #  Теперь придется это делать через createsuperuser или админку.
    #  path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
