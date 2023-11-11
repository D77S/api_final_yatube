from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # superuser: login/pass admin1/admin1
    # "refresh": ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl" +
    # "IjoicmVmcmVzaCIsImV4cCI6MTY5OTgwOTAzNCwianRpIjoiNDI4ZDlkNmRkYjQyNDI" +
    # "zNmEwYzA3ZTU0NWZlYjQ2MTIiLCJ1c2VyX2lkIjoxfQ.hcrZ4Da5MGjQsHHocjfGwz89x4ShJjYTUrTol3GxVmc"),
    # "access": ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlI" +
    # "joiYWNjZXNzIiwiZXhwIjoxNzA4Mjc2MjM0LCJqdGkiOiJkOTU3NTU5ZDhiNDY0NW" +
    # "FkYmVhMzhjMTMxYTU0NDE0MyIsInVzZXJfaWQiOjF9.fasM8ylNDVU8-uTt53c2z1ghNnjwAuu-p0wXt-7LO2Q")
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
