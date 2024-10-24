from rest_framework.routers import DefaultRouter
from api_v1.views.auto import AutoViewSet, MarcaViewSet

router = DefaultRouter()
router.register(r'autos', AutoViewSet, 'autos')
router.register(r'marcas', MarcaViewSet, 'marcas')



urlpatterns = router.urls