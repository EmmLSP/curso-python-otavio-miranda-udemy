"""
Exercicio 015
Crie um programa que crie uma matriz de dimensao 3x3 e
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatacao
correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)
print(matriz)
for linha in matriz:
    for i, num in enumerate(linha):
        if i < len(linha) - 1:
            print(f'[{num:^5}] ', end='')
        else:
            print(f'[{num:^5}]')
