from rest_framework import serializers
from .models import Farmacia, HorarioSemanal#, EscalaPlantao

class HorarioSemanalSerializer(serializers.ModelSerializer):
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
            'domingoHorarioFechamento'
        )

class FarmaciaSerializer(serializers.ModelSerializer):

    horarioSemanal = HorarioSemanalSerializer(many=True, read_only=True)

    class Meta:
        model = Farmacia
        fields = (
            'id', 
            'nome', 
            'razao_social', 
            'cnpj', 'whatsapp', 
            'telefone', 
            'email', 
            'plantonista', 
            'url_image', 
            'horarioSemanal'
        )

# class EscalaPlantaoSerializer(serializers.ModelSerializer):
    
#     farmacia = FarmaciaSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = EscalaPlantao
#         fields = ['id', 'dia_hora_inicio', 'dia_hora_fechamento', 'farmacia']