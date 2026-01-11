"""
Exercicio 010
Crie um programa que vai ler varios numeros e colocar
em uma lista.
Depois disso, mostre:

A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou nao na lista.
"""

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    if resp == 'N':
        break

print('-=' * 30)
valores.sort(reverse=True)
print(f'Voce digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!\nNas posições ', end='')
    for pos, valor in enumerate(valores):
        if valor == 5:
            print(f'{pos}... ', end='')
    print()
else:
    print('O valor 5 nao foi encontrado na lista!')
