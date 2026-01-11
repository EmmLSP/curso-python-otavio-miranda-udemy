"""
Exercicio 011
Crie um programa que vai ler varios numeros e
colocar em uma lista.
Depois disso, crie duas listas extras que vao
conter apenas os valores pares e os valores 
impares digitados, respectivamente.
Ao final, mostre o conteudo das tres listas
geradas.
"""

numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    if resp == 'N':
        break

for v in numeros:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('-=' * 30)
print(f'Lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
