from rest_framework.routers import DefaultRouter

from . import views

# register router
router_user = DefaultRouter()
router_user.register(r'', viewset=views.UserViewSet, basename='users')
