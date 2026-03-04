import os
import json
import random
from datetime import datetime, timedelta
import pandas as pd

# =========================
# CONFIGURAÇÕES
# =========================

DATA_INICIO_CARGA = datetime(2026, 1, 1)
CAMINHO_METADATA = "control_metadata.json"
CAMINHO_PEDIDOS = "landing_zone/pedidos.csv"

PEDIDOS_POR_DIA = 5


# =========================
# FUNÇÕES AUXILIARES
# =========================

def carregar_metadata():
    if not os.path.exists(CAMINHO_METADATA):
        return None

    with open(CAMINHO_METADATA, "r") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return None
        return json.loads(conteudo)


def salvar_metadata(metadata):
    with open(CAMINHO_METADATA, "w") as f:
        json.dump(metadata, f, indent=4)


def gerar_pedidos_para_data(data, id_inicial):
    pedidos = []
    id_atual = id_inicial

    for _ in range(PEDIDOS_POR_DIA):
        id_atual += 1

        pedido = {
            "id_pedido": id_atual,
            "data_pedido": data.strftime("%Y-%m-%d"),
            "id_cliente": random.randint(1, 20),
            "valor_total": round(random.uniform(50, 500), 2)
        }

        pedidos.append(pedido)

    return pedidos, id_atual


# =========================
# LÓGICA PRINCIPAL
# =========================

def main():

    hoje = datetime.today().date()
    metadata = carregar_metadata()

    # =========================
    # PRIMEIRA EXECUÇÃO
    # =========================

    if metadata is None:

        print("Primeira execução detectada.")

        metadata = {
            "pedidos": {
                "ultimo_id": 0,
                "ultima_data_processada": None
            },
            "itens_pedido": {
                "ultima_execucao": None
            },
            "clientes": {},
            "produtos": {}
        }

        data_atual = DATA_INICIO_CARGA.date()
        todos_pedidos = []
        ultimo_id = 0

        while data_atual <= hoje:
            pedidos_dia, ultimo_id = gerar_pedidos_para_data(data_atual, ultimo_id)
            todos_pedidos.extend(pedidos_dia)
            data_atual += timedelta(days=1)

        df = pd.DataFrame(todos_pedidos)
        df.to_csv(CAMINHO_PEDIDOS, index=False)

        metadata["pedidos"]["ultimo_id"] = ultimo_id
        metadata["pedidos"]["ultima_data_processada"] = hoje.strftime("%Y-%m-%d")

        salvar_metadata(metadata)

        print("Carga inicial finalizada.")
        return

    # =========================
    # EXECUÇÕES POSTERIORES
    # =========================

    ultima_data = metadata["pedidos"]["ultima_data_processada"]
    ultimo_id = metadata["pedidos"]["ultimo_id"]

    if ultima_data is None:
        raise Exception("Metadata inconsistente.")

    ultima_data = datetime.strptime(ultima_data, "%Y-%m-%d").date()

    # Reprocessamento do mesmo dia
    if ultima_data == hoje:

        print("Reprocessamento do dia atual.")

        df_existente = pd.read_csv(CAMINHO_PEDIDOS)
        df_existente = df_existente[df_existente["data_pedido"] != hoje.strftime("%Y-%m-%d")]

        novos_pedidos, ultimo_id = gerar_pedidos_para_data(hoje, ultimo_id)

        df_novo = pd.DataFrame(novos_pedidos)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)

        df_final.to_csv(CAMINHO_PEDIDOS, index=False)

    # Novo dia (incremental)
    elif ultima_data < hoje:

        print("Carga incremental detectada.")

        nova_data = ultima_data + timedelta(days=1)

        novos_pedidos, ultimo_id = gerar_pedidos_para_data(nova_data, ultimo_id)

        df_novo = pd.DataFrame(novos_pedidos)

        df_novo.to_csv(CAMINHO_PEDIDOS, mode="a", header=False, index=False)

    metadata["pedidos"]["ultimo_id"] = ultimo_id
    metadata["pedidos"]["ultima_data_processada"] = hoje.strftime("%Y-%m-%d")

    salvar_metadata(metadata)

    print("Execução finalizada com sucesso.")


if __name__ == "__main__":
    main()
