from rest_framework.routers import DefaultRouter

from electronics.views import NetworkNodeViewSet, ProductViewSet

app_name = "electronics"

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"networknodes", NetworkNodeViewSet)

urlpatterns = []

urlpatterns += router.urls
