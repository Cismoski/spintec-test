from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Spintec Test API Swagger",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=tuple(),
)

urlpatterns = [
    path('api/', include('web.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
