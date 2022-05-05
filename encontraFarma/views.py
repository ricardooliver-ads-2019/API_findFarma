from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from datetime import datetime
from rest_framework.decorators import action

from encontraFarma.models import Farmacia, EscalaPlantao
from .serializer import EscalaPlantaoSerializer, FarmaciaSerializer, FarmaciasPlantaoSerializer
from .repository import busca_farmacias_plantao_agora, busca_farmacias_horario_comercial_agora


class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer


class BuscaFarmaciasPlantaoAgoraViewSet(viewsets.ReadOnlyModelViewSet):    
    serializer_class = FarmaciasPlantaoSerializer    

    def get_queryset(self):
        pass

    def list(self, request):
        lista_de_farmacias = busca_farmacias_plantao_agora()

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        
        return Response(serializer.data)      


class BuscaFarmaciasHorarioComercialAgoraViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FarmaciaSerializer
    
    def get_queryset(self):
        pass

    def list(self, request):                               
        lista_de_farmacias = busca_farmacias_horario_comercial_agora()      

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        
        return Response(serializer.data)      


class BuscaEscalaFarmaciaPlantaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EscalaPlantao.objects.all()
    serializer_class = EscalaPlantaoSerializer

    @action(detail=True, methods=["get"])
    def farmacia_plantao(self, request, pk=None):
        
        data_atual = datetime.now().strftime("%G-%m-%d")
        
        escala = EscalaPlantao.objects.filter(farmacia=pk, data_hora_inicio_plantao__date__gte=data_atual)
        serializer = self.get_serializer(escala, many=True)

        return Response(serializer.data)


class BuscaEscalaFarmaciaPlantaoPorDataEspecificaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FarmaciasPlantaoSerializer

    def get_queryset(self):
        pass

    def list(self, request):        
        data = request.query_params["data"]   
        
        escala = EscalaPlantao.objects.filter(data_hora_inicio_plantao__date=f"{data}")

        serializer = self.get_serializer(escala, many=True)

        return Response(serializer.data)


class DataHoraServidorViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request):       
        hora_atual = datetime.now().strftime("%H:%M")
        data_atual = datetime.now().strftime("%Y-%m-%d")

        data_hora = {
            "data": data_atual,
            "hora": hora_atual,
            "data-hora": f'{data_atual} {hora_atual}',
        }

        content = JSONRenderer().render(data_hora)        
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream) 
        
        return Response(data)