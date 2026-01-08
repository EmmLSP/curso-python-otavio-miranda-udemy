# Concatenando e estendendo listas em Python

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    polimorfismo - sinal de '+' se comportar de outra
maneira com outro tipo de dado
None - nao valor ou sem retorno
Create | Read | Update  | Delete
Criar  | ler  | Alterar | apagar = lista[i] = (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
# lista_d = lista_a.extend(lista_b)
#print(lista_d) None (nao retorna nada)
lista_a.extend(lista_b)
print(lista_a) # a lista_a para a lista_b
