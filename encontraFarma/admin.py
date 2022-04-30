from django.contrib import admin

from .forms import PessoaFormAdmin
from .models import Farmacia, EscalaPlantao


@admin.register(Farmacia)
class FarmaciasAdmin(admin.ModelAdmin):
    form = PessoaFormAdmin

    class Media:
        js = ("jquery.mask.min.js", "custom.js")

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
    )


@admin.register(EscalaPlantao)
class EscalaPlantao(admin.ModelAdmin):
    list_display = (
        'id',
        'data_hora_inicio_plantao',        
        'data_hora_final_plantao',        
    )