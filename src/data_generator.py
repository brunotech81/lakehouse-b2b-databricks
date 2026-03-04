import pandas as pd
from faker import Faker
import random
import os 
# Funcionar em português pt-br
fake = Faker("pt_BR")
# ----------------------------------------
SEGMENTOS = ["bar","restaurante","mercado"]

ESTADOS = {
    "MG": ["BELO HORIZONTE","UBERLANDIA","CONTAGEM"],
    "SP": ["SÃO PAULO","CAMPINAS","GUARULHOS"],
    "RJ": ["RIO DE JANEIRO","SÃO GONÇALO","DUQUE DE CAXIAS"],
    "ES": ["VITÓRIA","VILA VELHA", "SERRA"]
}

SUFIXOS_EMPRESA = ["LTDA","EIRELI","ME"]

# Clientes

def gerar_clientes(qtd_clientes):
    clientes = []
    for i in range (1, qtd_clientes +1):
        estado = random.choice(list(ESTADOS.keys()))
        cidade = random.choice(ESTADOS[estado])
        segmento = random.choice(SEGMENTOS)
        nome_fantasia = fake.word().capitalize()
        sufixo = random.choice(SUFIXOS_EMPRESA)
        nome_empresa = f"{segmento.capitalize()} {nome_fantasia} {sufixo}"
        data_cadastro = fake.date_between(start_date="-4y", end_date="today")
        cliente = {
            "id_cliente" : i,
            "nome_da_empresa" : nome_empresa,
            "segmento" : segmento,
            "estado" : estado,
            "cidade" : cidade,
            "data_cadastro" : data_cadastro  
        }
        clientes.append(cliente)    
    return pd.DataFrame(clientes)

# Gerar lista
if __name__ == "__main__": 
    df_clientes = gerar_clientes(10)
    os.makedirs("landing_zone", exist_ok=True)
    caminho_arquivo = "landing_zone/clientes.csv"
    df_clientes.to_csv(caminho_arquivo, index=False)
    print (f"Arquivo gerado: {caminho_arquivo}")

