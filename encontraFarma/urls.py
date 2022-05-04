from encontraFarma.views import (
    DataHoraServidorViewSet, 
    FarmaciasViewSet, 
    BuscaFarmaciasPlantaoAgoraViewSet, 
    BuscaFarmaciasHorarioComercialAgoraViewSet,
)
    #, FarmaciasAbertasViewSet, FarmaciasPlantaoHojeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('busca-farmacias', FarmaciasViewSet)
router.register('busca-farmacias-plantao-agora', BuscaFarmaciasPlantaoAgoraViewSet, basename='farmacias-plantao-agora')
router.register('busca-farmacias-horario-comercial-agora', BuscaFarmaciasHorarioComercialAgoraViewSet, basename='busca-farmacias-horario-comercial-agora')
#router.register('busca-farmacias-plantao/id', FarmaciasViewSet, basename='busca-farmacias')
# router.register('busca-farmacias-plantao?data=', FarmaciasPlantaoHojeViewSet, basename='farmacia-plantao-por-data') 
router.register('busca-data-hora-servidor', DataHoraServidorViewSet, basename='data-hora-servidor')