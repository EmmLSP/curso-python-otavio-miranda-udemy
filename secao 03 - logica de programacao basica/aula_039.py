# Exercício guiado com while

"""
Iterando strings com while
----------------------------------------
|   0   1  2  3  4  5  6  7  8  9  10  |
|   L   u  i  z     O  t  a  v  i   o  |
| -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1  |
----------------------------------------

strings sao iteravveis
"""

nome = 'Luiz Otavio'
print(nome[0]) # L
print(nome[-11]) # L

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    if indice < tamanho_nome - 1:
        novo_nome += f'*{letra}' # acumulador += f'*{letra}'
    else:
        novo_nome += f'*{letra}*' # acumulador += f'*{letra}*'
    indice += 1

print(novo_nome)
