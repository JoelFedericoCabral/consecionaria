from rest_framework.routers import DefaultRouter

from api_v1.views.auto import AutoViewSet

router = DefaultRouter()
router.register(r'autos', AutoViewSet, 'autos')

urlpatterns = router.urls