import pandas as pd
import numpy as np
import html5lib

nomes_f = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json')

nomes_m = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')

# Agrupa os dataframes
frames = [nomes_f, nomes_m]
df_alunos = pd.concat(frames)['nome'].to_frame()

total_alunos = len(df_alunos)

# Cria ids aleatórios entre 1 e 400
np.random.seed(123)
df_alunos['id_aluno'] = np.random.permutation(total_alunos) + 1 # Soma 1 para não ter id 0
df_alunos = df_alunos.set_index('id_aluno')

# Cria e-mail par cada aluno a partir dos domínios
dominios = ['@gmail.com', '@yahoo.com', '@outlook.com', '@terra.com.br', '@hotmail.com']
df_alunos['dominio_email'] = np.random.choice(dominios, total_alunos) # Atribui os domínios de forma aleatória

df_alunos['email'] = df_alunos.nome.str.cat(df_alunos.dominio_email).str.lower()

# Exporta csv com a lista dos alunos
# nomes.to_csv('nomes_alunos.csv', sep=';', index=False)


url = 'https://tabela-cursos.herokuapp.com/index.html'
lista_cursos = pd.read_html(url)

# Cria dataframe de cursos
df_cursos = lista_cursos[0]

df_cursos = df_cursos.rename(columns={'Nome do curso': 'nome_do_curso'})

df_cursos['id_curso'] = df_cursos.index + 1

df_cursos = df_cursos.set_index('id_curso')

print(df_alunos.sort_values('id_aluno'))