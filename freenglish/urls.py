from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="UserRoom API Documentation",
      default_version='v1',
      description="Link for google login http://localhost:8000/accounts/login/google/",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your-email@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('userroom.urls')),
    path('accounts/', include('accounts.urls')),

    # Swagger UI route
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc route
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
