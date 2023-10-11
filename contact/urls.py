from rest_framework.routers import DefaultRouter

from . import views

# register router
router_client = DefaultRouter()
router_client.register(r'', viewset=views.ClientViewSet, basename='Client')
