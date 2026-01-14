# Exercício - exiba os índices da lista (aula com solução)

"""
Exercicio
Exiba os indices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')
lista.append('Anna')
lista.append('Pedro')

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
print()

for indice in range(len(lista)):
    print(indice, lista[indice], type(lista[indice]))
print()

for i, nome in enumerate(lista):
    print(i, nome, type(nome))
