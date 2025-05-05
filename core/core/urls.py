from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('root.urls')),
    path('accounts/', include('accounts.urls')), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    #
    path('api/swg/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)