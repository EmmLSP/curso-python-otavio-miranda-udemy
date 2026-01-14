"""
Exercicio 016
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('-=' * 30)
for m in matriz:
    for i, v in enumerate(m):
        print(f'[{v:^5}] ', end='')
    print()
print('-=' * 30)

soma_pares = soma_3c = maior_2l = 0
for l in range(len(matriz)):
    for c in range(len(matriz)):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        # if c == 2:
        #     soma_3c += matriz[l][2]
        # b if  l == 0 or matriz[1][c] > maior_2l:
        #     maior_2l = matriz[1][c]

print(f'A soma valores pares é {soma_pares}')
for l in range(0, 3):
    soma_3c += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_3c}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior_2l:
        maior_2l = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_2l}')
