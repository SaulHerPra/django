from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .api import router

api_version=settings.API_VERSION

urlpatterns = [
    #path('hola/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls'))
    path(f'api/{api_version}/',include((router.urls,'api'),namespace='api'))
]