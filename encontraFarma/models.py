from django.db import models

    # def busca_farmacias_plantao_hoje():
    #     data_hora_atual = datetime.now().strftime("%G-%m-%d %X")
        
    #     query = f'SELECT * FROM encontraFarma_escalaplantao WHERE "{data_hora_atual}" >= data_hora_inicio_plantao AND "{data_hora_atual}" <= data_hora_final_plantao'
        
    #     farmacias = HorarioSemanal.objects.raw(query)
        
    #     lista_de_farmacias = []
    #     for f in farmacias:
    #         lista_de_farmacias.append(f.farmacia)

    #     return lista_de_farmacias

    # def busca_farmacias_plantao_por_data_recebida(data_recebida):        
    #     query = f'SELECT * FROM encontraFarma_escalaplantao WHERE "{data_recebida}" >= DATE(data_hora_inicio_plantao) AND "{data_recebida}" <= DATE(data_hora_final_plantao)'
     
    #     farmacias = HorarioSemanal.objects.raw(query)
        
    #     lista_de_farmacias = []
    #     for f in farmacias:
    #         lista_de_farmacias.append(f.farmacia)

    #     return lista_de_farmacias


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
        return self.nome


#     def busca_farmacias_abertas():
#         nome_dia_semana = datetime.now().strftime("%A")
#         hora_atual = datetime.now().strftime("%X")
                
#         query = retorna_query_busca_farmacia_dia_semana(nome_dia_semana, hora_atual)
#         farmacias = HorarioSemanal.objects.raw(query)
        
#         lista_de_farmacias = []
#         for f in farmacias:
#             lista_de_farmacias.append(f.farmacia)

#         return lista_de_farmacias

    
class EscalaPlantao(models.Model):
    data_hora_inicio_plantao = models.DateTimeField()
    data_hora_final_plantao = models.DateTimeField()
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
       
    def __str__(self):         
        return f'{self.data_hora_inicio_plantao} :: {self.data_hora_final_plantao}'