# Inserindo itens em qualquer índice da lista com insert (Tipo list)

"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - extende a lista
    + - concatena listas
Create | Read | Update  | Delete
Criar  | ler  | Alterar | apagar = lista[i] = (CRUD)
"""

#       -4  -3  -2  -1
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz') # adionado
print(lista)
nome = lista.pop() # removido
print(lista, nome)

lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista, lista.pop())

# del() - apagar item da lista
lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista)
nome = lista.pop()
print(lista, nome)
lista.append(1234)
print(lista)
del lista[4] # ultimo item da lista
print(lista)

# del() - apagar item da lista
lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista)
nome = lista.pop()
print(lista, nome)
lista.append(1234)
print(lista)
print('Tamanho da lista:', len(lista) - 1)
del lista[len(lista) - 1] # ultimo item da lista
print(lista)

# del() - apagar item da lista
lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista)
nome = lista.pop()
print(lista, nome)
lista.append(1234)
print(lista)
del lista[-1] # ultimo item da lista
print(lista)

# clear() -> limpar a lista
lista = [10, 20, 30, 40]
print(lista)
lista.clear()
print(lista)

# insert() -> metodo que recebe 2 argumentos (indice, valor)
lista = [10, 20, 30, 40]
print(lista)
lista.insert(0, 5)
print(lista)

# erro - tentar acessar item que nao existe
lista = [10, 20, 30, 40]
print(lista)
lista.insert(0, 5)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
# print(lista[5])
# IndexError: list index out of range
print('-' * 15)
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
# print(lista[-6])
# IndexError: list index out of range
print('-' * 15)

lista = [10, 20, 30, 40]
lista.insert(100, 5) # falha do Python
# print(lista[100])
# IndexError: list index out of range
print(lista[-1])
print(lista[4])
