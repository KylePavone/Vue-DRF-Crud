from django.urls import path
from rest_framework import routers
from .views import PlayersViewSet


router = routers.DefaultRouter()
router.register('players', PlayersViewSet)

urlpatterns = router.urls
