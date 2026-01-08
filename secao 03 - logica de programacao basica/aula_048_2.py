# Alterando uma lista com índices, del, append e pop (Tipo list)

"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis:
    append, insert, pop, del, clear, extend, +
Create | Read | Update  | Delete
Criar  | ler  | Alterar | apagar = lista[i] = (CRUD)
"""

lista = []
print(lista, bool(lista)) # [] False

#       -4  -3  -2  -1
#        0   1   2   3
lista = [10, 20, 30, 40] # lista de inteiro
print(lista)
print(lista[2])  # 30
print(lista[-2]) # 30

# read - ler
lista = [10, 20, 30, 40]
numero = lista[2]
print(numero)

# upate - alterar
lista = [10, 20, 30, 40]
lista[2] = 300
print(lista)
print(lista[2])

# delete - apagar
lista = [10, 20, 30, 40]
# todo lugar que referenciar na lista
# vai ser mudado o valor para ser alterado
# depois que linha que foi alterada
lista[2] = 300
print('antes  del', lista)
del lista[2]
print('depois del', lista)
# o Python reorganizou os indices da lista
print(lista[2]) # indice 2 -> 40

# E interessante adicionar ou retirar coisas do final da lista
# caso contrario se for do inicio vai exigir muito processamento
# deixando lento o programa

# em Python tudo e um objeto, existe acoes que fazem coisas na lista
# metodo append() -> adcionar ao final da lista
lista = [10, 20, 30, 40]
print(lista)
# 50 adicionado ao final da lista
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

# pop() -> remove ultimo elemento da lista
lista = [10, 20, 30, 40]
print(lista)
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, ' pop() -> removido:', ultimo_valor, ' do tipo:', type(ultimo_valor))

# pop(indice) -> remove indice da lista, passando indice
lista = [10, 20, 30, 40]
print(lista)
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
valor_indice_3 = lista.pop(3)
print(lista, ' pop(3) -> removido:', valor_indice_3)

# evirtar remover item do meio ou inicio da lista se ela for muito grande
