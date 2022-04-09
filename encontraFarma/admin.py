from django.contrib import admin
from .models import Farmacia, HorarioSemanal#, EscalaPlantao


@admin.register(HorarioSemanal)
class HorariosSemanalAdmin(admin.ModelAdmin):
    model = HorarioSemanal
    list_display = ('id', 'farmacia')

@admin.register(Farmacia)
class FarmaciasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'razao_social',
        'telefone',
        'email',
        'plantonista',
        'cnpj', 
        'whatsapp',
        'url_image', 
        'responsavel', 
        'horarioSemanal'
    )