import pandas as pd
import numpy as np
import html5lib
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, MetaData, Table, inspect

nomes_f = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json')

nomes_m = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')

# Agrupa os dataframes
frames = [nomes_f, nomes_m]
df_alunos = pd.concat(frames)['nome'].to_frame()

total_alunos = len(df_alunos)

# Cria ids aleatórios entre 1 e 400
np.random.seed(123)
df_alunos['id_aluno'] = np.random.permutation(total_alunos) + 1 # Soma 1 para não ter id 0


# Cria e-mail par cada aluno a partir dos domínios
dominios = ['@gmail.com', '@yahoo.com', '@outlook.com', '@terra.com.br', '@hotmail.com']
df_alunos['dominio_email'] = np.random.choice(dominios, total_alunos) # Atribui os domínios de forma aleatória

df_alunos['email'] = df_alunos.nome.str.cat(df_alunos.dominio_email).str.lower()


# Exporta csv com a lista dos alunos
# nomes.to_csv('nomes_alunos.csv', sep=';', index=False)


url = 'https://tabela-cursos.herokuapp.com/index.html'
lista_cursos = pd.read_html(url)

df_cursos = lista_cursos[0] # Cria dataframe de cursos

df_cursos = df_cursos.rename(columns={'Nome do curso': 'nome_do_curso'})

df_cursos['id_curso'] = df_cursos.index + 1

df_cursos = df_cursos.set_index('id_curso')



df_alunos['qtd_matriculas'] = np.ceil(np.random.exponential(size=total_alunos) * 1.5).astype(int) # Cria a quantidade de matrículas para cada aluno

# graf_matriculas = sns.displot(df_alunos['qtd_matriculas'])
# graf_matriculas.set(xlabel='Qtd. de matrículas', ylabel='Qtd. de alunos')
# plt.show()

# qtd_matriculas_alunos = df_alunos['qtd_matriculas'].value_counts()


# Atribui cursos aos alunos
matriculas_aluno = []
x = np.random.rand(df_cursos.shape[0])
prob = x / sum(x)

for index, row in df_alunos.iterrows():
    id = row.id_aluno
    matriculas = row.qtd_matriculas
    cont = 0
    cursos_aluno = []
    while cont < matriculas:
        curso = np.random.choice(df_cursos.index, p=prob)
        if(curso not in cursos_aluno):
            matriculas_aluno.append([id, curso])
            cursos_aluno.append(curso)
            cont += 1

df_matriculas_alunos = pd.DataFrame(matriculas_aluno, columns=['id_aluno', 'id_curso'])
# df_matriculas_alunos.to_csv('matriculas_alunos.csv', sep=';', index=False)

df_matriculas_cursos = df_matriculas_alunos.groupby('id_curso').count().join(df_cursos['nome_do_curso']).rename(columns={'id_aluno': 'qtd_de_alunos'})
# df_matriculas_cursos.to_csv('matriculas_cursos.csv', sep=';', index=False)


# Cria o banco SQL
engine = create_engine('sqlite:///:memory:') # SQLite salvando na memória local

df_matriculas_cursos.to_sql('matriculas_cursos', engine) # Cria a tabela matriculas_cursos no banco

df_alunos.to_sql('alunos', engine)

df_cursos.to_sql('cursos', engine)

inspector = inspect(engine) # Cria um inspector object para o banco

query_1= 'select * from matriculas_cursos where nome_do_curso like "%mysql%"'
query_1r = pd.read_sql(query_1, con=engine) # r = read

query_matriculas = pd.read_sql_table('matriculas_cursos', engine, columns=['nome_do_curso', 'qtd_de_alunos'])
query_matriculasr = query_matriculas.query('nome_do_curso.str.contains("MySql")')

# print(inspector.get_table_names())

query_2= 'select * from alunos where qtd_matriculas >= 9'
query_2r = pd.read_sql(query_2, con=engine)


# Cria e exporta as listas de alunos por curso
lista_id_cursos = list(df_cursos.index)


for id_curso in lista_id_cursos:
    id = id_curso
    nome_curso = df_cursos['nome_do_curso'].loc[id]

    lista_alunos_curso = df_matriculas_alunos.query('id_curso == {}'.format(id))
    lista_alunos_curso = lista_alunos_curso.set_index('id_aluno').join(df_alunos.set_index('id_aluno'))['nome'].to_frame()

    lista_alunos_curso = lista_alunos_curso.rename(columns={'nome': 'Alunos do curso de {}'.format(nome_curso)})
    lista_alunos_curso.to_csv('lista_alunos_curso_{}.csv'.format(nome_curso).lower(), sep=';')
