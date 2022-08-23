import pandas as pd

dataset = pd.read_csv('aluguel.csv', delimiter=';')

# Informações sobre as base de dados
# print(dataset.dtypes)

tipos_dados = pd.DataFrame(dataset.dtypes, columns=['Tipos de dados'])
tipos_dados.columns.name = 'Variáveis'
# print(tipos_dados)

# Qtd. de registros e variáveis
linhas_colunas = dataset.shape
# print('A base de dados apresenta {} registros e {} variáveis'.format(linhas_colunas[0], linhas_colunas[1]))
