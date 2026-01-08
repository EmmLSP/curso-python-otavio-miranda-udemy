# Tipo list - Introdução às listas mutáveis em Python

"""
Listas em Python
Tipo List - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
string -> cadeia de caracteres, semelhante a lista
string -> tipo de dado imutavel
Obs.: Python le da esquerda para direita
e de cima para baixo
"""

#         01234
#        -54321
string = 'ABCDE' # 5 caracteres

print(string[2])  # C
print(string[-3]) # C

# lista = list()
lista = []
print(len(lista)) # 0 caracter
print(lista, type(lista)) # lista do tipo list

lista = [] # '' -> lista vazia
print(bool(lista)) # False

#        0     1     2             3    4
#       -5    -4    -3            -2   -1
lista = [123, True, 'Luiz Otavio', 1.2, []]
print(bool(lista)) # True
print(lista)

# acessar o indice de uma string dentro
# de uma lista acessando seu indice
print(lista[2])      # indice da lista a partir do 0
print(lista[2][3])   # indice da lista e da string a partir do 0
print(lista[-3])     # indice da lista a partir do -1
print(lista[-3][-8]) # indice da lista e da string a partir do -1

print(lista[2].upper(), type(lista[2]))
print(lista[2].lower(), type(lista[2]))
print(lista[-3].upper(), type(lista[-3]))
print(lista[-3].lower(), type(lista[-3]))

# Alterar valores da lista
lista = [123, True, 'Luiz Otavio', 1.2, []]
print('Antes  :', lista)
lista[-3] = 'Maria'
print('Depois :', lista)
print(lista[2], type(lista[2]))
