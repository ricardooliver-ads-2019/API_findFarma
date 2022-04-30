from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from datetime import datetime

from encontraFarma.models import Farmacia, EscalaPlantao
from .serializer import FarmaciaSerializer, FarmaciaComPlantaoSerializer
from .repository import busca_farmacias_abertas_horario_comercial, busca_farmacias_abertas_plantao

class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer


class FarmaciasAbertasPlantaoViewSet(viewsets.ReadOnlyModelViewSet):    
    serializer_class = FarmaciaComPlantaoSerializer
    
    def list(self, request):       
                        
        lista_de_farmacias = busca_farmacias_abertas_plantao()      

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        
        return Response(serializer.data)      


class FarmaciasAbertasHorarioComercialViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FarmaciaSerializer
    
    def list(self, request):       
                        
        lista_de_farmacias = busca_farmacias_abertas_horario_comercial()      

        serializer = self.get_serializer(lista_de_farmacias, many=True)
        
        return Response(serializer.data)      

# class FarmaciasAbertasViewSet(viewsets.ReadOnlyModelViewSet):    
#     queryset = Farmacia.objects.all()
#     serializer_class = FarmaciaSerializer
    
#     def list(self, request): 
#         lista_de_farmacias = Farmacia.busca_farmacias_abertas()        

#         serializer = self.get_serializer(lista_de_farmacias, many=True)
#         return Response(serializer.data)      


# class FarmaciasPlantaoHojeViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = EscalaPlantao.objects.all()
#     serializer_class = FarmaciaPlatonistaSerializer

#     def list(self, request):
#         lista_de_farmacias = EscalaPlantao.busca_farmacias_plantao_hoje()

#         serializer = self.get_serializer(lista_de_farmacias, many=True)
#         return Response(serializer.data)    

# class FarmaciasPlantaoPorDataRecebida(viewsets.ReadOnlyModelViewSet):
#     serializer_class = FarmaciaPlatonistaSerializer

#     def list(self, request):
#         data = request.query_params["data"]                
#         lista_de_farmacias = EscalaPlantao.busca_farmacias_plantao_por_data_recebida(data_recebida=data)

#         serializer = self.get_serializer(lista_de_farmacias, many=True)
#         return Response(serializer.data)   


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