import pandas as pd

# Ver o dataframe completo
# pd.set_option('display.max_rows', 500)

dataset = pd.read_csv('db.csv', sep = ';')

# print(dataset)

# Conjunto de estatíticas descritivas
estat_carros = dataset[['Quilometragem', 'Valor']].describe()
# print(estat_carros)


dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })

    return result

carros = pd.DataFrame(km_media(dados, 2019)).T
print(carros)
