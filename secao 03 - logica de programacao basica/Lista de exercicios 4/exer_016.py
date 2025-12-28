"""
Exercicio 016
Refaca o desafio de PA do Mundo 2, lendo o primeiro
termo e a razao de uma PA, mostrando os 10 primeiros
termos da progressao usando a estrutura while.
"""

# primeiro + (10 - 1) * razao

print('Gerador de PA')
print('-=' * 15)

primeiro = int(input('Primeiro termo: ')) 
razao = int(input('Razao da PA: '))
decimo = primeiro + (10 - 1) * razao
while primeiro <= decimo:
    print(primeiro, end='')
    print(' -> ' if primeiro < decimo else '\n', end='') 
    primeiro += razao

primeiro = int(input('Primeiro termo: ')) 
razao = int(input('Razao da PA: '))
termo = primeiro
c = 0
while c < 10:
    print(termo, end='')
    print(' -> ' if c < 9 else '\n', end='') 
    termo += razao
    c += 1
