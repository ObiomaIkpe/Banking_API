from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from core_apps.user_auth.views import TestLoggingView
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", TestLoggingView.as_view(), name="home"),
    
    path("api/v1/auth/", include('djoser.urls')),
    path("api/v1/auth/", include('core_apps.user_auth.urls'))
]
