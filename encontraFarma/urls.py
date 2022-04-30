from email.mime import base
from encontraFarma.views import (
    DataHoraServidorViewSet, 
    FarmaciasViewSet, 
    FarmaciasAbertasPlantaoViewSet, 
    FarmaciasAbertasHorarioComercialViewSet
)
    #, FarmaciasAbertasViewSet, FarmaciasPlantaoHojeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('busca-farmacias', FarmaciasViewSet)
router.register('busca-farmacias-abertas-plantao', FarmaciasAbertasPlantaoViewSet, basename='farmacias-abertas-plantao')
router.register('busca-farmacias-abertas-horario-comercial', FarmaciasAbertasHorarioComercialViewSet, basename='farmacias-abertas-horario-comercial')
#router.register('busca-farmacias-plantao/id', FarmaciasViewSet, basename='busca-farmacias')
# router.register('busca-farmacias-plantao?data=', FarmaciasPlantaoHojeViewSet, basename='farmacia-plantao-por-data') 
router.register('busca-data-hora-servidor', DataHoraServidorViewSet, basename='data-hora-servidor')