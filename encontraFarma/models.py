from django.db import models
import datetime

# class EscalaPlantao(models.Model):
#     farmacia = models.ForeignKey(Farmacia, related_name='escalaPlantao', on_delete=models.CASCADE)
#     dia_hora_inicio = models.DateTimeField()
#     dia_hora_fechamento = models.DateTimeField()

#     def __str__(self):
#         return f'{self.dia_hora_inicio}'

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
        return f'Horário Semanal {self.id}' 


class Farmacia(models.Model):
    nome = models.CharField(max_length=60)
    razao_social = models.CharField(max_length=60, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)
    whatsapp = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    plantonista = models.BooleanField()
    url_image = models.URLField(null=True, blank=True)
    responsavel = models.CharField(max_length=60, null=True, blank=True)

    horarioSemanal = models.OneToOneField(HorarioSemanal, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome