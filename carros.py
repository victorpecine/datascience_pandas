import pandas as pd

# Ver o dataframe completo
# pd.set_option('display.max_rows', 500)

dataset = pd.read_csv('db.csv', sep = ';')

print(dataset)

# Conjunto de estatíticas descritivas
estat_carros = dataset[['Quilometragem', 'Valor']].describe()
print(estat_carros)