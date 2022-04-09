from encontraFarma.views import FarmaciasViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('farmacias-abertas', FarmaciasViewSet)