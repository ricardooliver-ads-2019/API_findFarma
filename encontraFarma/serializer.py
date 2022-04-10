from dataclasses import field
from rest_framework import serializers
from .models import Farmacia, HorarioSemanal, EscalaPlantao

class HorarioSemanalSerializer(serializers.ModelSerializer):
    
    farmacia = serializers.StringRelatedField()

    class Meta:
        model = HorarioSemanal
        fields = (
            'id',
            'segunda_horario_abertura',
            'segunda_horario_fechamento',
            'terca_horario_abertura',
            'terca_horario_fechamento',
            'quarta_horario_abertura',
            'quarta_horario_fechamento',
            'quinta_horario_abertura',
            'quinta_horario_fechamento',
            'sexta_horario_abertura', 
            'sexta_horario_fechamento',
            'sabado_horario_abertura',
            'sabado_horario_fechamento',
            'domingo_horario_abertura',
            'domingo_horario_fechamento',
            'farmacia'
        )


class FarmaciaSerializer(serializers.ModelSerializer):   

    horario_semanal = HorarioSemanalSerializer()

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
            'horario_semanal'            
        )


class EscalaPlantaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EscalaPlantao
        fields = (
            'id',
            'data_hora_inicio_plantao',
            'data_hora_final_plantao' 
        )



class FarmaciaPlatonistaSerializer(serializers.ModelSerializer):   

    escala_plantao = EscalaPlantaoSerializer(many=True)

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
            'escala_plantao'                    
        )        