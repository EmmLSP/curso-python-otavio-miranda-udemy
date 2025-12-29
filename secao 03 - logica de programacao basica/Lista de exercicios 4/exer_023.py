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
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 15)
total = 0
vitorias = 0
while True:
    computador = randint(0, 5)
    jogador = int(input('Digite um valor: '))
    opcao = input('PAR ou IMPAR? [P/I] ').upper()
    if opcao == 'P':
        total = jogador + computador
        print('-' * 30)
        print(f'Voce jogou {jogador} e o computador {computador}. ', end='')
        print(f'Total de {total} ', end='')
        if total % 2 == 0:
            print('DEU PAR')
            print('-' * 30)
            print('Voce VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            vitorias += 1
        else:
            print('DEU IMPAR')
            print('-' * 30)
            print('Voce PERDEU!')
            print('-=' * 15)
            break
    elif opcao == 'I':
        total = jogador + computador
        print('-' * 30)
        print(f'Voce jogou {jogador} e o computador {computador}. ', end='')
        print(f'Total de {total} ', end='')
        if total % 2 == 1:
            print('DEU IMPAR')
            print('-' * 30)
            print('Voce VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            vitorias += 1
        else:
            print('DEU PAR')
            print('-' * 30)
            print('Voce PERDEU!')
            print('-=' * 15)
            break
    else:
        print('Opcao invalida!')

if vitorias == 1:
    print(f'GAMER OVER! Voce venceu {vitorias} vez.')
else:
    print(f'GAMER OVER! Voce venceu {vitorias} vezes.')
