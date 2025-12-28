"""
Exercicio 020
Crie um programa que leia varios numeros inteiros
pelo teclado. No final da execucao, mostre a media
entre todos os valores e qual foi o maior e menor
valores lidos. O programa deve perguntar ao usuario
se ele quer ou nao continuar a digitar valores.
"""

from time import sleep

soma = maior = menor = cont = 0
continuar = True
while continuar:

    num = int(input('Digite um numero: '))
    soma += num
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1

    valida_resp = False
    while not valida_resp:
        resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if resp in 'SN':
            valida_resp = True
        else:
            print('Entrada invalida! Digite \'S\' ou \'N\'')
    
    if resp == 'N':
        print('Finalizando...')
        sleep(1)
        continuar = False

media = soma / cont

print('-' * 30)
print(f'Voce digitou {cont} numeros e a media foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
