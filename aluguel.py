import pandas as pd

dataset = pd.read_csv('aluguel.csv', sep=';')

# Informações sobre as base de dados
# print(dataset.dtypes)
# print(dataset)

# tipos_dados = pd.DataFrame(dataset.dtypes, columns=['Tipos de dados'])
# tipos_dados.columns.name = 'Variáveis'
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


# Identificando dados nulos
# print(dataset.info())

# Visualizando registros nulos
dataset_valores_nulos = (dataset['Valor'].isnull()) | (dataset['Condominio'].isnull()) | (dataset['IPTU'].isnull())
# print(dataset[dataset_valores_nulos])


# Alterando valores nulos para 0
dataset = dataset.fillna({'Valor':0, 'Condominio': 0, 'IPTU': 0})
# print(dataset)

# dataset.to_csv('aluguel.csv', sep=';', index=False)
# dados_residencial.to_csv('dados_residencial.csv', sep=';', index=False)


# Criando novas variáveis
dados_residencial['Valor bruto'] = dados_residencial['Valor'] + dados_residencial['Condominio'] + dados_residencial['IPTU']

dados_residencial['Valor/m2'] = (dados_residencial['Valor'] / dados_residencial['Area']).round(2)

# Excluindo registros com Valor = 0
dados_residencial.drop(dados_residencial[dados_residencial['Valor'] == 0].index, inplace=True)

# print(dados_residencial.sort_values(by=['Valor/m2'], ascending=False))


# Agrupando tipos entre Casa ou Apartamento
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
dados_residencial['Tipo agregado'] = dados_residencial['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')

# print(dados_residencial)

del dados_residencial['Valor bruto']

# print(dados_residencial)

# dados_residencial.to_csv('dados_residencial.csv', sep=';', index=False)

# Contagem de tipos

print('*'*30)

cont_tipos_dataset = dataset['Tipo'].value_counts()
print(cont_tipos_dataset)

print('*'*30)

cont_tipos_residencial = dados_residencial['Tipo'].value_counts()
print(cont_tipos_residencial)

print('*'*30)

bairros = dados_residencial.groupby('Bairro')
media_preco_bairros = bairros[['Valor', 'Condominio']].mean().round(2)

print(media_preco_bairros.sort_values(by=['Valor'], ascending=False))







alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

alunos_sexo = alunos.groupby()
media_notas_sexo = alunos_sexo[['Notas']].mean().roun(2)



sexo = alunos.groupby['Sexo']
sexo = pd.DataFrame(sexo['Notas'].mean().round(2))
sexo.columns = ['Notas Médias']


print(sexo)
