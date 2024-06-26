from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

# Swagger 설정
schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="API documentation for Todo app",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# DRF 라우터 설정
router = routers.DefaultRouter()



# URL 패턴 설정
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('todo.urls')),
]
