import pandas as pd
import random
import os
from datetime import datetime, timedelta


def gerar_pedidos():

    # Busca id_cliente da tabela clientes
    clientes_df = pd.read_csv("landing_zone/clientes.csv")
    lista_clientes = clientes_df["id_cliente"].tolist()

    data_inicio = datetime(2026, 1, 1)
    data_fim = datetime.today()

    delta_dias = (data_fim - data_inicio).days

    pedidos = []
    id_pedido = 1

    # Distribuição de status
    status_opcoes = ["entregue", "aprovado", "pendente", "cancelado"]
    pesos_status = [0.7, 0.15, 0.1, 0.05]

    for i in range(delta_dias + 1):

        data_atual = data_inicio + timedelta(days=i)

        # Entre 80 e 120 pedidos por dia
        qtd_pedidos_dia = random.randint(80, 120)

        for _ in range(qtd_pedidos_dia):

            id_cliente = random.choice(lista_clientes)

            status = random.choices(status_opcoes, weights=pesos_status)[0]

            pedidos.append({
                "id_pedido": id_pedido,
                "id_cliente": id_cliente,
                "data_pedido": data_atual.strftime("%Y-%m-%d"),
                "status": status
            })

            id_pedido += 1

    df = pd.DataFrame(pedidos)

    return df


def salvar_csv(df):

    os.makedirs("landing_zone", exist_ok=True)

    caminho_arquivo = "landing_zone/pedidos.csv"

    df.to_csv(caminho_arquivo, index=False)

    print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
    print(f"Total de pedidos gerados: {len(df)}")


if __name__ == "__main__":

    df_pedidos = gerar_pedidos()

    print(df_pedidos.head())

    salvar_csv(df_pedidos)
