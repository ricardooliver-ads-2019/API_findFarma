import numbers

from django.db import models
from datetime import datetime

SEGUNDA = "Monday"
TERCA = "Tuesday"
QUARTA = "Wednesday"
QUINTA = "Thursday"
SEXTA = "Friday"
SABADO = "Saturday"
DOMINGO = "Sunday"

class HorarioSemanal(models.Model):

    segunda_horario_abertura = models.TimeField(null=True, blank=True)
    segunda_horario_fechamento = models.TimeField(null=True, blank=True)
    terca_horario_abertura = models.TimeField(null=True, blank=True)
    terca_horario_fechamento = models.TimeField(null=True, blank=True)
    quarta_horario_abertura = models.TimeField(null=True, blank=True)
    quarta_horario_fechamento = models.TimeField(null=True, blank=True)
    quinta_horario_abertura = models.TimeField(null=True, blank=True)
    quinta_horario_fechamento = models.TimeField(null=True, blank=True)
    sexta_horario_abertura = models.TimeField(null=True, blank=True)
    sexta_horario_fechamento = models.TimeField(null=True, blank=True)
    sabado_horario_abertura = models.TimeField(null=True, blank=True)
    sabado_horario_fechamento = models.TimeField(null=True, blank=True)
    domingo_horario_abertura = models.TimeField(null=True, blank=True)
    domingo_horario_fechamento = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        if hasattr(self, "farmacia"):                 
            return f'{self.farmacia}' 
        return f'{self.pk}'
           

class EscalaPlantao(models.Model):
    data_hora_inicio_plantao = models.DateTimeField()
    data_hora_final_plantao = models.DateTimeField()
       
    def __str__(self):         
        return f'{self.data_hora_inicio_plantao} :: {self.data_hora_final_plantao}'        

    def busca_farmacias_plantao_hoje():
        data_hora_atual = datetime.now().strftime("%G-%m-%d %X")
        
        query = f'SELECT * FROM encontraFarma_escalaplantao WHERE "{data_hora_atual}" >= data_hora_inicio_plantao AND "{data_hora_atual}" <= data_hora_final_plantao'
        
        farmacias = HorarioSemanal.objects.raw(query)
        
        lista_de_farmacias = []
        for f in farmacias:
            lista_de_farmacias.append(f.farmacia)

        return lista_de_farmacias


class Farmacia(models.Model):
    nome = models.CharField(max_length=60)
    razao_social = models.CharField(max_length=60, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    whatsapp = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    cep = models.CharField(max_length=8, null=True, blank=True,)
    rua = models.CharField(max_length=60, null=True, blank=True,)
    numero = models.IntegerField(default=0, null=True, blank=True,)
    bairro = models.CharField(max_length=60, null=True, blank=True,)
    cidade = models.CharField(max_length=60, null=True, blank=True,)
    uf = models.CharField(max_length=2, null=True, blank=True,)
    plantonista = models.BooleanField()
    url_image = models.URLField(null=True, blank=True, unique=True)
    responsavel = models.CharField(max_length=60, null=True, blank=True)
    cpf_responsavel = models.CharField(max_length=11, null=True, blank=True)
    horario_semanal = models.OneToOneField(HorarioSemanal, unique=True, on_delete=models.CASCADE, related_name="farmacia")
    escala_plantao = models.ManyToManyField(EscalaPlantao, null=True, blank=True)

    def __str__(self):
        return self.nome

    def busca_farmacias_abertas():
        nome_dia_semana = datetime.now().strftime("%A")
        hora_atual = datetime.now().strftime("%X")
                
        query = retorna_query_busca_farmacia_dia_semana(nome_dia_semana, hora_atual)
        farmacias = HorarioSemanal.objects.raw(query)
        
        lista_de_farmacias = []
        for f in farmacias:
            lista_de_farmacias.append(f.farmacia)

        return lista_de_farmacias

    
def retorna_query_busca_farmacia_dia_semana(nome_dia_semana, hora_atual):
    
    query = ""
    if nome_dia_semana == DOMINGO:            
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= domingo_horario_abertura AND "{hora_atual}" <= domingo_horario_fechamento'
        return query
    
    if nome_dia_semana == SEGUNDA:
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= segunda_horario_abertura AND "{hora_atual}" <= segunda_horario_fechamento'
        return query
    
    if nome_dia_semana == TERCA:
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= terca_horario_abertura AND "{hora_atual}" <= terca_horario_fechamento'
        return query
    
    if nome_dia_semana == QUARTA:
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= quarta_horario_abertura AND "{hora_atual}" <= quarta_horario_fechamento'
        return query
    
    if nome_dia_semana == QUINTA:
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= quinta_horario_abertura AND "{hora_atual}" <= quinta_horario_fechamento'
        return query
    
    if nome_dia_semana == SEXTA:
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= sexta_horario_abertura AND "{hora_atual}" <= sexta_horario_fechamento'
        return query
    
    if nome_dia_semana == SABADO:
        query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= sabado_horario_abertura AND "{hora_atual}" <= sabado_horario_fechamento'
        return query