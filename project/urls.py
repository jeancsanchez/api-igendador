from django.contrib import admin
from django.urls import path, include

from event import routers as event_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(event_router.router.urls)),
]
