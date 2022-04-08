from rest_framework import viewsets
from .models import Farmacia, HorarioSemanal#, EscalaPlantao
from .serializer import FarmaciaSerializer, HorarioSemanalSerializer#, EscalaPlantaoSerializer

class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer

    # def busca_farmacias_plantao(self):
    #     EscalaPlantao.objects.filter()
    #     Farmacia.objects.filter()


class HorarioSemanalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HorarioSemanal.objects.all()
    serializer_class = HorarioSemanalSerializer


# class EscalaPlantaoViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = EscalaPlantao.objects.all()
#     serializer_class = EscalaPlantaoSerializer