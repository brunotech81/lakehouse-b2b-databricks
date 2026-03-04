import pandas as pd

df = pd.read_csv("landing_zone/clientes.csv")

print(df.head())
print("\nQuantidade de linhas:")
print(len(df))
print("\nInformações do DataFrame:")
print(df.info())
