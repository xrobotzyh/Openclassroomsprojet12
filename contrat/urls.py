from rest_framework.routers import DefaultRouter

from . import views

# register router
router_contract = DefaultRouter()
router_contract.register(r'', viewset=views.ContratViewSet, basename='Contract')
