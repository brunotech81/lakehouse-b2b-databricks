import pandas as pd
import random
import os

def gerar_produtos():

    categorias = {
        "cerveja": {
            "marcas": ["Skol", "Antarctica", "Brahma"],
            "volumes": ["350ml", "473ml", "600ml"],
            "preco_min": 4.00,
            "preco_max": 10.00
        },
        "refrigerante": {
            "marcas": ["H2OH", "Pepsi"],
            "volumes": ["350ml", "2L"],
            "preco_min": 5.00,
            "preco_max": 9.00
        },
        "vinho": {
            "marcas": ["Dante Robino", "Bodega"],
            "volumes": ["750ml"],
            "preco_min": 35.00,
            "preco_max": 90.00
        },
        "energético": {
            "marcas": ["Fusion Energy Drink"],
            "volumes": ["473ml"],
            "preco_min": 8.00,
            "preco_max": 15.00
        }
    }

    produtos = []
    id_produto = 1

    # Pelo menos 1 produto por categoria
    for categoria, info in categorias.items():

        marca = random.choice(info["marcas"])
        volume = random.choice(info["volumes"])
        preco = round(random.uniform(info["preco_min"], info["preco_max"]), 2)

        nome_produto = f"{categoria.capitalize()} {marca} {volume}"

        produtos.append({
            "id_produto": id_produto,
            "nome_produto": nome_produto,
            "categoria": categoria,
            "marca": marca,
            "preco_unitario": preco
        })

        id_produto += 1

    # Produto extra aleatório
    categoria_extra = random.choice(list(categorias.keys()))
    info = categorias[categoria_extra]

    marca = random.choice(info["marcas"])
    volume = random.choice(info["volumes"])
    preco = round(random.uniform(info["preco_min"], info["preco_max"]), 2)

    nome_produto = f"{categoria_extra.capitalize()} {marca} {volume}"

    produtos.append({
        "id_produto": id_produto,
        "nome_produto": nome_produto,
        "categoria": categoria_extra,
        "marca": marca,
        "preco_unitario": preco
    })

    df = pd.DataFrame(produtos)

    return df


def salvar_csv(df):

    
    os.makedirs("landing_zone", exist_ok=True)

    caminho_arquivo = "landing_zone/produtos.csv"

    df.to_csv(caminho_arquivo, index=False)

    print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")


if __name__ == "__main__":

    df_produtos = gerar_produtos()

    print(df_produtos)

    salvar_csv(df_produtos)
