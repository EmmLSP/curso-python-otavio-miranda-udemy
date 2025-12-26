"""
Exercicio 006
Desenvolva um programa que leia o primeiro
termo e a razao de uma PA. No final, mostre
os 10 primeiros termos dessa progressao.

formula: an = a1 + (n - 1) * r

primeiro termo = 2
razao = 3
termos = 10
=> 2 5 8 11 14 17 20 23 26 29
"""

print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c} -> ', end='')
print('ACABOU')

print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = 0
for c in range(0, 10):
    pa = primeiro + (c * razao)
    print(pa, end=' -> ')
print('ACABOU')

print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
for c in range(0, 10):
    print(primeiro, end=' -> ')
    primeiro += razao
print('ACABOU')
