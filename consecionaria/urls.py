from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

# Rutas estándar que no necesitan internacionalización
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api_v1/', include('api_v1.urls')),
    # Ruta para permitir el cambio de idioma
    path('set-language/', set_language, name='set_language'),
]

# Rutas con soporte para internacionalización
urlpatterns += i18n_patterns(
    path('', include('home.urls')), 
    path('gestion/', include('gestion.urls')),
    prefix_default_language=False  # Esto evita que el idioma predeterminado aparezca en la URL
)

# Rutas para servir archivos estáticos y de medios en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
