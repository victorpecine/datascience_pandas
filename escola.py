import pandas as pd

nomes_f = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json')
amostra_nomes_f = nomes_f.sample(5)

nomes_m = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')
amostra_nomes_m = nomes_m.sample(5)

# Agrupando os datasets
frames = [nomes_f, nomes_m]
nomes = pd.concat(frames)['nome'].to_frame()

