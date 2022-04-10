from encontraFarma.views import FarmaciasViewSet, FarmaciasAbertasViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('farmacias', FarmaciasViewSet)
router.register('farmacias-abertas', FarmaciasAbertasViewSet)