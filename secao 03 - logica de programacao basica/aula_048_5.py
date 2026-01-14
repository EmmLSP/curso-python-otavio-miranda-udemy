# Cuidados com tipos de dados mutáveis - list e copy

"""
Cuidados com dados mutaveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""

# nome = 'Luiz'
# nome[1]  = 'D'
# TypeError: 'str' object does not support item assignment

# 'Luiz' vai ser eliminado por garbage colection,
# robo do Python que faz a limpeza de coisas que
# nao estao sendo utilizadas
nome = 'Luiz' 
nome = 'Joao'
print(nome)

# lista_a e lista_b estao apontando para o mesmo
# lugar na memoria, mesmo id

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # faz uma copia da lista_a na lista_b

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
