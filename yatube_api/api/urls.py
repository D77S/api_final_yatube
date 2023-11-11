from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet  # , CommentViewSet, CommentViewSet

router_v1 = routers.DefaultRouter()
# router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
# router_v1.register(r'posts/(?P<post_id>\d+)/comments',
#                    CommentViewSet,
#                    basename='comments'
#                    )

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    # superuser: login/pass admin1/admin1
    # "refresh": ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl" +
    # "IjoicmVmcmVzaCIsImV4cCI6MTY5OTgwOTAzNCwianRpIjoiNDI4ZDlkNmRkYjQyNDI" +
    # "zNmEwYzA3ZTU0NWZlYjQ2MTIiLCJ1c2VyX2lkIjoxfQ.hcrZ4Da5MGjQsHHocjfGwz89x4ShJjYTUrTol3GxVmc"),
    # "access": ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlI" +
    # "joiYWNjZXNzIiwiZXhwIjoxNzA4Mjc2MjM0LCJqdGkiOiJkOTU3NTU5ZDhiNDY0NW" +
    # "FkYmVhMzhjMTMxYTU0NDE0MyIsInVzZXJfaWQiOjF9.fasM8ylNDVU8-uTt53c2z1ghNnjwAuu-p0wXt-7LO2Q")
    path('v1/', include(router_v1.urls)),
]
