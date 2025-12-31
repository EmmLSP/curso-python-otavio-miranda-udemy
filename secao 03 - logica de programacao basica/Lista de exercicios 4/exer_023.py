"""
Exercicio 023
Faca um programa que jogue par ou impar com
o computador. O jogo so sera interrompido
quando o jogador PERDER, mostrando o total
de vitorias consecutivas que ele conquistou
no final do jogo.
"""

from random import randint

print('-=' * 15)
print(f'{'VAMOS JOGAR PAR OU IMPAR':^30}')
print('-=' * 15)
total = 0
vitorias = 0
while True:
    computador = randint(0, 10)
    while True:
        jogador = int(input('Digite um valor: '))
        if jogador < 0 or jogador > 10:
            print('Valor invalido! Digite um valor entre 1 e 10')
            continue
        break
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('PAR ou IMPAR? [P/I] ').strip().upper()[0]
        if tipo in 'PI':
            break
        print('Tipo invalido! Digite \'P\' ou \'I\'')
    total = jogador + computador
    print('-' * 30)
    print(f'Voce jogou {jogador} e o computador {computador}. ', end='')
    print(f'Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR') # if simplificado
    print('-' * 30)
    if tipo == 'P': 
        if total % 2 == 0:
            print('Voce VENCEU!')
            vitorias += 1
        else:
            print('Voce PERDEU!')  
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!') 
            vitorias += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-=' * 15)

print('-=' * 15)
if vitorias == 1:
    print(f'GAMER OVER! Voce venceu {vitorias} vez.')
else:
    print(f'GAMER OVER! Voce venceu {vitorias} vezes.')
