"""
Exercicio 046
Em uma competicao de salto em distancia cada atleta tem direito a 
cinco saltos. No final da serie de saltos de cada atleta, o melhor 
e o pior resultados sao eliminados. O seu resultado fica sendo a 
media dos tres valores restantes. Voce deve fazer um programa que 
receba o nome e as cinco distancias alcancadas pelo atleta em seus 
saltos e depois informe a media dos saltos conforme a descricao acima 
informada (retirar o melhor e o pior salto e depois calcular a media).
Faca uso de uma lista para armazenar os saltos. Os saltos sao informados 
na ordem da execucao, portanto nao sao ordenados. O programa deve ser 
encerrado quando nao for informado o nome do atleta. A saida do programa 
deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Corvello
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor Salto: 6.5 m
Pior Salto: 5.3 m
Media dos demais saltos: 5.9 m

Resultado final:
Rodrigo Corvello: 5.9 m
"""

from time import sleep
from os import system

melhor_salto = pior_salto = 0
soma_saltos_restantes = media_saltos_restantes = 0
while True:
    saltos = []
    atleta = input('Digite o nome do atleta: ')
    for s in range(5):
        distancia = float(input(f'Digite a distancia do {s + 1} salto: '))
        saltos.append(distancia)

        if s == 0:
            melhor_salto = pior_salto = distancia
        else:
            if distancia > melhor_salto:
                melhor_salto = distancia
            if distancia < pior_salto:
                pior_salto = distancia
    
    soma_saltos_restantes = 0
    for s in range(5):
        if saltos[s] == pior_salto:
            soma_saltos_restantes += 0
        elif saltos[s] == melhor_salto:
            soma_saltos_restantes += 0
        else:
            soma_saltos_restantes += saltos[s]
    media_saltos_restantes = soma_saltos_restantes / 3

    print('\nDistancias dos Saltos:')
    print('[', end='')
    for s in range(5):
        if s < len(saltos) - 1:
            print(f'{saltos[s]}, ', end='')
        else:
            print(f'{saltos[s]}]')
        
    print(f'\nAtleta: {atleta}')
    print(f'Primeiro Salto: {saltos[0]} m')
    print(f'Segundo Salto: {saltos[1]} m')
    print(f'Terceiro Salto: {saltos[2]} m')
    print(f'Quarto Salto: {saltos[3]} m')
    print(f'Quinto Salto: {saltos[4]} m')
    print()
    print(f'melhor salto: {melhor_salto} m')
    print(f'pior salto: {pior_salto} m')
    print(f'Media dos demais saltos: {media_saltos_restantes:.1f} m')
    print()
    print('Resultado final:')
    print(f'{atleta}: {media_saltos_restantes:.1f} m')
    print('-' * 30)

    while True:
        continuar = input('Quer continuar? [S]im [N]ao: ').upper()
        if continuar == 'S' or continuar == 'N':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    
    if continuar == 'S':
        system('cls')
        continue
    
    if continuar == 'N':
        print('Encerrando...')
        sleep(1)
        break

print('-' * 30)
print('<<< Fim do Programa >>>')
