from encontraFarma.views import FarmaciasPlantaoPorDataRecebida, FarmaciasViewSet, FarmaciasAbertasViewSet, FarmaciasPlantaoHojeViewSet, DataHoraServidorViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('farmacias', FarmaciasViewSet)
router.register('farmacias-abertas', FarmaciasAbertasViewSet)
router.register('farmacias-plantao-hoje', FarmaciasPlantaoHojeViewSet)
router.register('farmacias-plantao-por-data', FarmaciasPlantaoPorDataRecebida, basename='farmacia-plantao-por-data')
router.register('data-hora-servidor', DataHoraServidorViewSet, basename='data-hora-servidor')