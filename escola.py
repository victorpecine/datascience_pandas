import pandas as pd
import numpy as np

nomes_f = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json')

nomes_m = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')

# Agrupa os dataframes
frames = [nomes_f, nomes_m]
nomes = pd.concat(frames)['nome'].to_frame()

total_alunos = len(nomes)

# Cria ids aleatórios entre 1 e 400
np.random.seed(123)
nomes['id_aluno'] = np.random.permutation(total_alunos) + 1 # Soma 1 para não ter id 0

# Cria e-mail par cada aluno a partir dos domínios
dominios = ['@gmail.com', '@yahoo.com', '@outlook.com', '@terra.com.br', '@hotmail.com']
nomes['dominio_email'] = np.random.choice(dominios, total_alunos) # Atribui os domínios de forma aleatória

nomes['email'] = nomes.nome.str.cat(nomes.dominio_email).str.lower()

nomes.to_csv('nomes_alunos.csv', sep=';', index=False)