from rest_framework import serializers
from .models import Farmacia, HorarioSemanal

class HorarioSemanalSerializer(serializers.ModelSerializer):
    
    farmacia = serializers.StringRelatedField()

    class Meta:
        model = HorarioSemanal
        fields = (
            'id',
            'segundaHorarioAbertura',
            'segundaHorarioFechamento',
            'tercaHorarioAbertura',
            'tercaHorarioFechamento',
            'quartaHorarioAbertura',
            'quartaHorarioFechamento',
            'quintaHorarioAbertura',
            'quintaHorarioFechamento',
            'sextaHorarioAbertura', 
            'sextaHorarioFechamento',
            'sabadoHorarioAbertura',
            'sabadoHorarioFechamento',
            'domingoHorarioAbertura',
            'domingoHorarioFechamento',
            'farmacia'
        )


class FarmaciaSerializer(serializers.ModelSerializer):   

    horarioSemanal = HorarioSemanalSerializer()

    class Meta:
        model = Farmacia
        fields = (
            'id', 
            'nome', 
            'razao_social', 
            'cnpj', 
            'whatsapp', 
            'telefone', 
            'email', 
            'plantonista', 
            'url_image', 
            'horarioSemanal'            
        )