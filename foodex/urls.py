from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Foodex API",
        default_version="v1",
        description="Documentación oficial del backend Foodex",
        contact=openapi.Contact(email="support@foodex.cl"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # API principal
    path("api/v1/", include("core.urls")),

    # Swagger
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]
