from django.db import models
import datetime
class Farmacia(models.Model):
    nome = models.CharField(max_length=60)
    razao_social = models.CharField(max_length=60)
    cnpj = models.CharField(max_length=18)
    whatsapp = models.CharField(max_length=14)
    telefone = models.CharField(max_length=13)
    email = models.EmailField()
    plantonista = models.BooleanField()
    url_image = models.URLField()

    def __str__(self):
        return self.nome


class EscalaPlantao(models.Model):
    farmacia = models.ForeignKey(Farmacia, related_name='escalaPlantao', on_delete=models.CASCADE)
    dia_hora_inicio = models.DateTimeField()
    dia_hora_fechamento = models.DateTimeField()

    def __str__(self):
        return f'{self.dia_hora_inicio}'


class DiasHorarioFuncionamento(models.Model):
    DIAS_SEMANAS_CHOICES = (
        ("SEG", 'SEGUNDA-FEIRA'),
        ("TER", 'TERÇA-FEIRA'),
        ("QUA", 'QUARTA-FEIRA'),
        ("QUI", 'QUINTA-FEIRA'),
        ("FEI", 'FEIRA-FEIRA'),
        ("SAB", 'SABADO-FEIRA'),
        ("DOM", 'DOMINGO-FEIRA'),
    )

    farmacia = models.ForeignKey(Farmacia,  related_name='diasHorarioFuncionamento', on_delete=models.CASCADE)

    dia_semana = models.CharField(choices=DIAS_SEMANAS_CHOICES, blank=False, null=False,max_length=3, unique=True)
    hora_inicio = models.TimeField()
    hora_fechamento = models.TimeField()

    def __str__(self):
        return self.dia_semana