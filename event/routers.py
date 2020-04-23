from rest_framework.routers import DefaultRouter

from event.views import EventViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'v1/events', EventViewSet)
