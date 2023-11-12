from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')
router_v1.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    # superuser: login/pass admin1/admin1
    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5OTkwMTEwMiwianRpIjoiMzE3ODZmNmIyOGY4NDkyYTgwYTMwZjI4NWFiMGQyMWIiLCJ1c2VyX2lkIjoxfQ.dk_UB3matd0Uk3AE_4J_Y4fFvNQlqbmQcJDd8HN3iUU"
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MzY4MzAyLCJqdGkiOiI1MjY0MWEwMWY1ZmI0MWRkODJjZjBkMzA5NjhmMGYzNiIsInVzZXJfaWQiOjF9.IPD8zFRGS9tMEZ4quYp6ziTmacpaxzoYUF9ZEcZeG-E"
    # admin2/admin2admin2
    # admin3/admin3admin3
    # admin4/admin4admin4
    # admin5/admin5admin5

    path('v1/', include(router_v1.urls)),
]
