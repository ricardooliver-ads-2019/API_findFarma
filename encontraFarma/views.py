from rest_framework import viewsets
from rest_framework.response import Response

from encontraFarma.models import Farmacia, EscalaPlantao
from .serializer import FarmaciaSerializer, FarmaciaPlatonistaSerializer

class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer


class FarmaciasAbertasViewSet(viewsets.ReadOnlyModelViewSet):    
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer
    
    def list(self, request): 
        lista_de_farmacias = Farmacia.busca_farmacias_abertas()        

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        return Response(serializer.data)      


class FarmaciasPlantaoHojeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EscalaPlantao.objects.all()
    serializer_class = FarmaciaPlatonistaSerializer

    def list(self, request):
        lista_de_farmacias = EscalaPlantao.busca_farmacias_plantao_hoje()

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        return Response(serializer.data)        