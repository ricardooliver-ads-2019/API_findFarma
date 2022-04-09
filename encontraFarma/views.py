from rest_framework import viewsets
from rest_framework.response import Response

from encontraFarma.models import Farmacia, HorarioSemanal
from .serializer import FarmaciaSerializer

class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer
    
    def list(self, request): 
        lista_de_farmacias = Farmacia.busca_farmacias_abertas()        

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        return Response(serializer.data)        