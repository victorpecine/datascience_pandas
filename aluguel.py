import pandas as pd

dataset = pd.read_csv('aluguel.csv', sep=';')

# Informações sobre as base de dados
# print(dataset.dtypes)

tipos_dados = pd.DataFrame(dataset.dtypes, columns=['Tipos de dados'])
tipos_dados.columns.name = 'Variáveis'
# print(tipos_dados)

# Qtd. de registros e variáveis
linhas_colunas = dataset.shape
# print('A base de dados apresenta {} registros e {} variáveis'.format(linhas_colunas[0], linhas_colunas[1]))


# Tipos de imóveis
tipos_imoveis = dataset['Tipo']
tipos_imoveis.drop_duplicates(inplace=True)
tipos_imoveis = pd.DataFrame(tipos_imoveis)

# print(tipos_imoveis)

tamanho_dataframe_tipos_imoveis = tipos_imoveis.shape[0]
# print(tamanho_dataframe_tipos_imoveis)

tipos_imoveis.index = range(tipos_imoveis.shape[0])
tipos_imoveis.columns.name = 'idTipo'
# print(tipos_imoveis)

# Identificando imóveis residenciais
residencial = ['Quitinete',
                'Casa',
                'Flat',
                'Apartamento',
                'Casa de Condomínio',
                'Casa de Vila',
                'Studio']

# Selecionando apenas os tipos residenciais
selecao_residencial = dataset['Tipo'].isin(residencial)

# Dataframe tipo residencial
dados_residencial = dataset[selecao_residencial]
dados_residencial.index = range(dados_residencial.shape[0])
# print(dados_residencial)

# Exportando a base de dados
dados_residencial.to_csv('dados_residencial.csv', sep=';', index=False)
