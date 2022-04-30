from datetime import datetime
from django.db import connection

SEGUNDA = "Monday"
TERCA = "Tuesday"
QUARTA = "Wednesday"
QUINTA = "Thursday"
SEXTA = "Friday"
SABADO = "Saturday"
DOMINGO = "Sunday"

def busca_farmacias_abertas_plantao():   
    data_hora_atual = datetime.now().strftime("%G-%m-%d %X")

    #TODO: Fazer consulta na tabela encontraFarma_escalaplantao
    rows = None
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM encontraFarma_farmacia INNER JOIN encontraFarma_escalaplantao ON 
            encontraFarma_farmacia.id=encontraFarma_escalaplantao.farmacia_id 
            WHERE ("{data_hora_atual}" >= encontraFarma_escalaplantao.data_hora_inicio_plantao AND 
            "{data_hora_atual}" <= encontraFarma_escalaplantao.data_hora_final_plantao)"""
        )        
        rows = dictfetchall(cursor)
    return rows


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
   

def busca_farmacias_abertas_horario_comercial(): 
    hora_atual = datetime.now().strftime("%X")
    nome_dia_semana = datetime.now().strftime("%A")

    horario = retorna_dia_semana_tabela_farmacia(nome_dia_semana)
    rows = None
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM encontraFarma_farmacia INNER JOIN encontraFarma_escalaplantao ON 
            encontraFarma_farmacia.id=encontraFarma_escalaplantao.farmacia_id 
            WHERE ("{hora_atual}" >= "{horario['abertura']}" AND "{hora_atual}" <= "{horario['fechamento']})"""
        )
        rows = dictfetchall(cursor)
    return rows


def retorna_dia_semana_tabela_farmacia(nome_dia_semana):
    horario = {
        "abertura": None,
        "fechamento": None
    }        

    if nome_dia_semana == DOMINGO:            
        horario["abertura"] = "domingo_horario_abertura"
        horario["fechamento"] = "domingo_horario_fechamento"

    elif nome_dia_semana == SEGUNDA:
        horario["abertura"] = "segunda_horario_abertura"
        horario["fechamento"] = "segunda_horario_fechamento"
        
    elif nome_dia_semana == TERCA:
        horario["abertura"] = "terca_horario_abertura"
        horario["fechamento"] = "terca_horario_fechamento"

    elif nome_dia_semana == QUARTA:
        horario["abertura"] = "quarta_horario_abertura"
        horario["fechamento"] = "quarta_horario_fechamento"

    elif nome_dia_semana == QUINTA:
        horario["abertura"] = "quinta_horario_abertura"
        horario["fechamento"] = "quinta_horario_fechamento"

    elif nome_dia_semana == SEXTA:
        horario["abertura"] = "sexta_horario_abertura"
        horario["fechamento"] = "sexta_horario_fechamento"

    elif nome_dia_semana == SABADO:
        horario["abertura"] = "sabado_horario_abertura"
        horario["fechamento"] = "sabado_horario_fechamento"

    return horario