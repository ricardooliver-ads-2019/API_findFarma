from rest_framework import viewsets
from .models import Farmacia
from .serializer import FarmaciaSerializer

class FarmaciasViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer

