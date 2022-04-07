from django.contrib import admin
from .models import Farmacia, DiasHorarioFuncionamento, EscalaPlantao


@admin.register(DiasHorarioFuncionamento)
class DiasHorarioFuncionamentoAdmin(admin.ModelAdmin):
    model = DiasHorarioFuncionamento
    list_display = ( 'id','dia_semana', 'hora_inicio', 'hora_fechamento')

@admin.register(Farmacia)
class FarmaciasAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','razao_sicial','telefone','email','plantonista', 'cnpj', 'whatsapp','url_image')

@admin.register(EscalaPlantao)
class EscalaPlantaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'farmacia', 'dia_hora_inicio', 'dia_hora_fechamento')