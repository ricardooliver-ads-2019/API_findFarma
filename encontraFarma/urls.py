from encontraFarma.views import FarmaciasViewSet, FarmaciasAbertasViewSet, FarmaciasPlantaoHojeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('farmacias', FarmaciasViewSet)
router.register('farmacias-abertas', FarmaciasAbertasViewSet)
router.register('farmacias-plantao-hoje', FarmaciasPlantaoHojeViewSet)