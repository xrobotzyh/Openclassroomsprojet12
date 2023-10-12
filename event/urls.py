from rest_framework.routers import DefaultRouter

from . import views
#register router
router_event = DefaultRouter()
router_event.register(r'', viewset=views.EventViewSet, basename='events')