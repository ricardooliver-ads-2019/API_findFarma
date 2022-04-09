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

    segundaHorarioAbertura = models.TimeField(null=True, blank=True)
    segundaHorarioFechamento = models.TimeField(null=True, blank=True)
    tercaHorarioAbertura = models.TimeField(null=True, blank=True)
    tercaHorarioFechamento = models.TimeField(null=True, blank=True)
    quartaHorarioAbertura = models.TimeField(null=True, blank=True)
    quartaHorarioFechamento = models.TimeField(null=True, blank=True)
    quintaHorarioAbertura = models.TimeField(null=True, blank=True)
    quintaHorarioFechamento = models.TimeField(null=True, blank=True)
    sextaHorarioAbertura = models.TimeField(null=True, blank=True)
    sextaHorarioFechamento = models.TimeField(null=True, blank=True)
    sabadoHorarioAbertura = models.TimeField(null=True, blank=True)
    sabadoHorarioFechamento = models.TimeField(null=True, blank=True)
    domingoHorarioAbertura = models.TimeField(null=True, blank=True)
    domingoHorarioFechamento = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        if hasattr(self, "farmacia"):                 
            return f'{self.farmacia}' 
        return f'{self.pk}'
           

class Farmacia(models.Model):
    nome = models.CharField(max_length=60)
    razao_social = models.CharField(max_length=60, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)
    whatsapp = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    plantonista = models.BooleanField()
    url_image = models.URLField(null=True, blank=True, unique=True)
    responsavel = models.CharField(max_length=60, null=True, blank=True)    

    horarioSemanal = models.OneToOneField(HorarioSemanal, unique=True, on_delete=models.CASCADE, related_name="farmacia")

    def __str__(self):
        return self.nome

    def busca_farmacias_abertas():
        nome_dia_semana = datetime.now().strftime("%A")
        hora_atual = datetime.now().strftime("%X")
        
        print(hora_atual)

        query = ""
        if nome_dia_semana == DOMINGO:            
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= domingoHorarioAbertura AND "{hora_atual}" <= domingoHorarioFechamento'
        
        elif nome_dia_semana == SEGUNDA:
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= segundaHorarioAbertura AND "{hora_atual}" <= segundaHorarioFechamento'
        
        elif nome_dia_semana == TERCA:
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= tercaHorarioAbertura AND "{hora_atual}" <= tercaHorarioFechamento'
        
        elif nome_dia_semana == QUARTA:
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= quartaHorarioAbertura AND "{hora_atual}" <= quartaHorarioFechamento'
        
        elif nome_dia_semana == QUINTA:
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= quintaHorarioAbertura AND "{hora_atual}" <= quintaHorarioFechamento'
        
        elif nome_dia_semana == SEXTA:
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= sextaHorarioAbertura AND "{hora_atual}" <= sextaHorarioFechamento'
        
        elif nome_dia_semana == SABADO:
            query = f'SELECT * FROM encontraFarma_horariosemanal WHERE "{hora_atual}" >= sabadoHorarioAbertura AND "{hora_atual}" <= sabadoHorarioFechamento'

        farmacias = HorarioSemanal.objects.raw(query)
        
        lista_de_farmacias = []
        for f in farmacias:
            lista_de_farmacias.append(f.farmacia)

        return lista_de_farmacias
    