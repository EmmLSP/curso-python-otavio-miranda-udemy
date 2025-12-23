"""
Exercicio 020
Altere o programa de calculo do fatorial, permitindo ao 
usuario calcular o fatorial varias vezes e limitando o 
fatorial a numeros inteiros positivos e menores que 16.
"""

from time import sleep

while True:
    num = int(input('Digite um numero para o fatorial: '))
    
    if num == 0:
        print(f'\nfatorial -> 0! = 1')
        continue

    print(f'\nfatorial -> {num}! = ', end='')
    fat = 1
    for n in range(num, 0, -1):
        fat *= n
        if n > 1:
            print(f'{n} x ', end='')
        else:
            print(f'{n} = {fat}')
        n -= 1
    print('-' * 30)

    valida_saida = False
    while not valida_saida:
        resp = input('Quer continuar? [S]im | [N]ao: ').upper()
        if resp == 'S' or resp == 'N':
            if resp == 'S':
                print()
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    
    if resp == 'N':
        print('-' * 30)
        print('ENCERRANDO...')
        sleep(1)
        break

print('<<< FIM DO PROGRAMA >>>')
