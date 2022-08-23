import pandas as pd

dataset = pd.read_csv('aluguel.csv', sep=';')

# Informações sobre as base de dados
# print(dataset.dtypes)
# print(dataset)

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
series_residencial = dataset['Tipo'].isin(residencial)

# Dataframe tipo residencial
dados_residencial = dataset[series_residencial]
dados_residencial.index = range(dados_residencial.shape[0])
# print(dados_residencial)

# Exportando a base de dados
# dados_residencial.to_csv('dados_residencial.csv', sep=';', index=False)


# Selecione somente os imóveis classificados com tipo 'Apartamento'
# df = dataframe
series_apartamentos = dados_residencial['Tipo'] == 'Apartamento'

df_apartamentos = dados_residencial[series_apartamentos].shape[0]
print('> {} apartamentos'.format(df_apartamentos))


# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'
series_casas = (dados_residencial['Tipo'] == 'Casa') | (dados_residencial['Tipo'] == 'Casa de Condomínio') | (dados_residencial['Tipo'] == 'Casa de Vila')

df_casas = dados_residencial[series_casas].shape[0]
print('> {} casas'.format(df_casas))


# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites
series_areas = (dados_residencial['Area'] >= 60) & (dados_residencial['Area'] <= 100)

df_areas = dados_residencial[series_areas].shape[0]
print('> {} imóveis com área entre 60 m² e 100 m²'.format(df_areas))


# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00
series_quartos_alugueis = (dados_residencial['Quartos'] >= 4) & (dados_residencial['Valor'] < 2000)

df_quartos_alugueis = dados_residencial[series_quartos_alugueis].shape[0]
print('> {} imóveis com, no mínimo, 4 quartos e aluguel abaixo de R$ 2.000,00'.format(df_quartos_alugueis))

# Lista dos imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00
# print(dados_residencial[series_quartos_alugueis])