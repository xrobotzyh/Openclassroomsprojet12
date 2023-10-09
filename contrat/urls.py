from rest_framework.routers import DefaultRouter

from . import views

# register router
router_contract = DefaultRouter()
router_contract.register(r'create', viewset=views.CreateContratViewSet, basename='Create Contract')