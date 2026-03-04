import os
import pandas as pd
import random

CAMINHO_PEDIDOS = "landing_zone/pedidos.csv"
CAMINHO_ITENS = "landing_zone/itens_pedido.csv"
CAMINHO_PRODUTOS = "landing_zone/produtos.csv"


def main():

    # Valida arquivos
    
    if not os.path.exists(CAMINHO_PEDIDOS):
        raise Exception("Arquivo pedidos.csv não encontrado.")

    if not os.path.exists(CAMINHO_PRODUTOS):
        raise Exception("Arquivo produtos.csv não encontrado.")

    pedidos_df = pd.read_csv(CAMINHO_PEDIDOS)
    produtos_df = pd.read_csv(CAMINHO_PRODUTOS)

    if not os.path.exists(CAMINHO_ITENS):
        print("Primeira geração de itens detectada.")
        pedidos_sem_itens = pedidos_df.copy()
        itens_existentes_df = pd.DataFrame()

    else:
        itens_existentes_df = pd.read_csv(CAMINHO_ITENS)

        pedidos_com_itens = set(itens_existentes_df["id_pedido"].unique())
        pedidos_sem_itens = pedidos_df[~pedidos_df["id_pedido"].isin(pedidos_com_itens)]

        print(f"Pedidos novos detectados: {len(pedidos_sem_itens)}")

    novos_itens = []

    for _, pedido in pedidos_sem_itens.iterrows():

        id_pedido = pedido["id_pedido"]

        # Quantidade de itens por pedido (1 a 5)
        qtd_itens = random.randint(1, 5)

        # Selecionar produtos sem repetição
        produtos_selecionados = produtos_df.sample(
            n=min(qtd_itens, len(produtos_df)),
            replace=False
        )

        for _, produto in produtos_selecionados.iterrows():

            item = {
                "id_pedido": id_pedido,
                "id_produto": produto["id_produto"],
                "quantidade": random.randint(1, 10),
                "valor_unitario": produto["valor_unitario"]
            }

            novos_itens.append(item)

    if not novos_itens:
        print("Nenhum item novo para gerar.")
        return

    novos_itens_df = pd.DataFrame(novos_itens)

    # Salvar resultado

    if os.path.exists(CAMINHO_ITENS):
        novos_itens_df.to_csv(
            CAMINHO_ITENS,
            mode="a",
            header=False,
            index=False
        )
    else:
        novos_itens_df.to_csv(
            CAMINHO_ITENS,
            index=False
        )

    print("Itens gerados com sucesso.")


if __name__ == "__main__":
    main()
