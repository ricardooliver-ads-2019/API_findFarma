from rest_framework import serializers
from .models import Farmacia


class FarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = ['id', 'nome', 'razao_social', 'cnpj', 'whatsapp', 'telefone', 'email', 'plantonista', 'url_image']