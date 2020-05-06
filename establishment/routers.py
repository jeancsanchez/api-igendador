from rest_framework.routers import DefaultRouter

from establishment.views import EstablishmentViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'v1/establishments', EstablishmentViewSet)
