from encontraFarma.models import HorarioSemanal
from encontraFarma.views import FarmaciasViewSet, HorarioSemanalViewSet#, EscalaPlantaoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('farmacias', FarmaciasViewSet)
router.register('horarios', HorarioSemanalViewSet)
#router.register('plantoes', EscalaPlantaoViewSet)