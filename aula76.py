# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


# pessoa = dict(nome="Leandro", sobrenome="Coutinho")

# pessoa = {
#     'nome': 'Leandro',
#     'sobrenome': 'Coutinho',
#     'idade': 23,
#     'altura': '1.65',
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }

# print(pessoa['nome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])

# # Apagando chaves

# pessoa['carro'] = 'HB20'
# print(pessoa)

# del pessoa['carro']
# print(pessoa)


# # Tentando acessar chave

# if pessoa.get('carro') is None:
#     print('Ñ existe')
# else:
#     print('Existe')

# pessoa = {
#     'nome': 'Leandro',
#     'sobrenome': 'Coutinho',
#     'idade': 900
# }

# print(pessoa.__len__())
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))


# for valor in pessoa.values():
#     print(valor)


# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])

# Apontam para o mesmo local na memória
# d1 = {
#     'c1': 1,
#     'c2': 2,
# }
# d2 = d1
# d2['c1'] = 1000
# print(d1)


# Shallow copy (Só copia valores imutáveis, se for uma lista ele aponta para o mesmo local)

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = d1.copy()

# d2['c1'] = 1000
# d2['l1'][1] = 9999
# print(d1)
# print(d2)

# Deep copy
# import copy


# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 9999
# print(d1)
# print(d2)

# Get

p1 = {
    'nome': 'Leandro',
    'sobrenome': 'Coutinho',
}

# print(p1.get('nome', 'Não existe'))

# Pop

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# Popitem (Exclui a última chave)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


# Update
# p1.update({
#     'nome':'novo valor',
#     'idade': 23,
# })

# print(p1)

# ou 

# p1.update(nome='novo valor', idade=30)
# print(p1)

# ou
tupla = ('nome', 'novo valor'), ('idade', 30)
p1.update(tupla)
print(p1)
