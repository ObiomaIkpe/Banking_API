from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)


from core_apps.user_auth.views import TestLoggingView
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", TestLoggingView.as_view(), name="home"),
    
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/schema/swagger-ui", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/v1/schema/redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/v1/auth/", include('djoser.urls')),
    path("api/v1/auth/", include('core_apps.user_auth.urls'))
]


admin.site.site_header = "Next Gen Bank Admin"
admin.site.site_title = "Next Gen Bank Admin Portal"
admin.site.site_index = "Welcome to Next Gen Bank Admin Portal"

