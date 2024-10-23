from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from home.views import custom_set_language

# Rutas estándar que no necesitan internacionalización
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api_v1/', include('api_v1.urls')),
    # Ruta para permitir el cambio de idioma
    path('set-language/', custom_set_language, name='set_language'),
]

# Rutas con soporte para internacionalización
urlpatterns += i18n_patterns(
    path('', include('home.urls')), 
    path('gestion/', include('gestion.urls')),
    prefix_default_language=False  # Evita que el idioma predeterminado (es) aparezca en la URL
)

# Rutas para servir archivos estáticos y de medios en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Configuración para asegurar que las URLs no forcen el idioma predeterminado
if not settings.USE_I18N:
    urlpatterns += [
        path('', include('home.urls')),  # Asegura que la URL raíz sin prefijo esté disponible
    ]
