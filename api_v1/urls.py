from rest_framework.routers import DefaultRouter
from api_v1.views.auto import AutoViewSet, MarcaViewSet, ComentarioViewSet, ClienteViewSet
from api_v1.views.user import UserViewSet

router = DefaultRouter()
router.register(r'autos', AutoViewSet, 'autos')
router.register(r'marcas', MarcaViewSet, 'marcas')
router.register(r'usuarios', UserViewSet, 'usuarios')
router.register(r'comentarios', ComentarioViewSet, 'comentarios')
router.register(r'clientes', ClienteViewSet, 'clientes')

urlpatterns = router.urls