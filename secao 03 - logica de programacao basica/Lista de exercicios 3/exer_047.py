"""
Exercicio 047
Em uma competicao de ginastica, cada atleta recebe
votos de sete jurados. Voce deve fazer um programa
que receba o nome do ginasta e a notas dos sete  
jurados alcancadas pelo atleta em sua apresentacao
e depois informe a sua media, conforme a descricao
acima informada (retirar o melhor e o pior salto e 
depois calcular a media com as notas restantes). As
notas nao sao informadas ordenadas. 
Um exemplo de saida do programa deve ser conforme o 
exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Media: 9.04
"""

from time import sleep
from os import system

melhor_nota = pior_nota = cont_atleta = 0
while True:
    notas = []
    soma_notas = 0
    cont_atleta += 1

    atleta = input('Digite o nome do ginasta: ')
    print(f'\nNome: {atleta} - atleta: {cont_atleta}:\n')
    for n in range(7):
        nota = float(input(f'Digite a nota {n+1}: '))
        notas.append(nota)
        if n == 0:
            melhor_nota = pior_nota = nota
        else:
            if nota > melhor_nota:
                melhor_nota = nota
            if nota < pior_nota:
                pior_nota = nota

    for n in range(7):
        if notas[n] == melhor_nota:
            soma_notas += 0
        elif notas[n] == pior_nota:
            soma_notas += 0
        else:
            soma_notas += notas[n] # 5 notas restantes
    media_notas = soma_notas / 5

    print('\nNotas:\n[', end='')
    for nota in range(len(notas)):
        if nota < len(notas) - 1:
            print(f'{notas[nota]}, ', end='')
        else:
            print(f'{notas[nota]}]\n')

    print(f'Atleta: {atleta}')
    print(f'Nota 1: {notas[0]}')
    print(f'Nota 2: {notas[1]}')
    print(f'Nota 3: {notas[2]}')
    print(f'Nota 4: {notas[3]}')
    print(f'Nota 5: {notas[4]}')
    print(f'Nota 6: {notas[5]}')
    print(f'Nota 7: {notas[6]}\n')

    print('Resultado final:')
    print(f'Atleta: {atleta}')
    print(f'Melhor nota: {melhor_nota}')
    print(f'Pior nota: {pior_nota}')
    print(f'Media: {media_notas:.2f}')

    while True:
        continuar = input('Quer continuar com proximo atleta? [S]im or [N]ao: ').upper()
        if continuar not in 'SN':
            print('Entrada invalida! Digite \'S\' ou \'N\'')
            continue
        break

    if continuar == 'S':
        system('cls')
        continue

    if continuar == 'N':
        print('Encerrando programa...')
        sleep(1)
        break

print('<<< PROGRAMA ENCERRADO >>>')
