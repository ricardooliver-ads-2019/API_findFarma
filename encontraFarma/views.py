from rest_framework import viewsets
from encontraFarma.models import Farmacia
from .serializer import FarmaciaSerializer

class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer