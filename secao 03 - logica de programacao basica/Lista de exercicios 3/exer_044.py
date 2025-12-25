"""
Exercicio 044
Em uma eleicao presidencial existem quatro candidatos.
Os votos sao informados por meio de codigo. Os codigos
utilizados sao:
1, 2, 3, 4 - Votos para os respectivos candidatos
(voce deve montar a tabela ex: 1 - Jose / 2 - Joao / etc)
5 - Voto nulo
6 - voto em branco
Faca um programa que calcule e mostre:
- O total de votos para cada candidato
- O total de votos nulos
- O total de votos em branco
- A percentagem de votos nulos sobre o total de votos
- A percentagem de votos em branco sobre o total de votos
Para finalizar o conjunto de votos tem-se o valor zero.

Regra de 3 para porcentagem de votos brancos:
total votos      100
votos brancos    x
--------------------
total votos * x = votos brancos * 100
x = (votos brancos * 100) / total votos
"""

from time import sleep

candidatos = ('Maria', 'Pedro', 'Anna', 'Joao')

print(f'''ELEICAO PRESIDENCIAL:
--------------------
NUMERO: 1 - {candidatos[0].upper()} 
NUMERO: 2 - {candidatos[1].upper()}
NUMERO: 3 - {candidatos[2].upper()} 
NUMERO: 4 - {candidatos[3].upper()}
NUMERO: 5 - Voto nulo 
NUMERO: 6 - Voto em branco
-------------------''')

votos_cand_1 = votos_cand_2 = votos_cand_3 = votos_cand_4 = 0
votos_nulo = votos_branco = total_votos = 0
percentagem_branco = percentagem_nulo = 0
cand_mais_votos = 0
candidato = ''
while True:

    num_voto = int(input('Escolha o numero do seu candidato: '))

    if num_voto == 1:
        votos_cand_1 += 1
        print(f'{votos_cand_1}x voto para {candidatos[0]}')
    elif num_voto == 2:
        votos_cand_2 += 1
        print(f'{votos_cand_2}x voto para {candidatos[1]}')
    elif num_voto == 3:
        votos_cand_3 += 1
        print(f'{votos_cand_3}x voto para {candidatos[2]}')
    elif num_voto == 4:
        votos_cand_4 += 1
        print(f'{votos_cand_4}x voto para {candidatos[3]}')
    elif num_voto == 5:
        votos_branco += 1
        print(f'{votos_branco}x votos em Branco')
    elif num_voto == 6:
        votos_nulo += 1
        print(f'{votos_nulo}x votos nulos')
    else:
        print('Entrada invalida! Digite numeros entre 1 e 6')
        continue
    total_votos += 1

    if total_votos == 1:
        cand_mais_votos = votos_cand_1 = votos_cand_2 = votos_cand_3 = votos_cand_4
    else:
        if votos_cand_1 > cand_mais_votos:
            cand_mais_votos = votos_cand_1
            candidato = f'{candidatos[0]} com {votos_cand_1} votos'
        if votos_cand_2 > cand_mais_votos:
            cand_mais_votos = votos_cand_2
            candidato = f'{candidatos[1]} com {votos_cand_2} votos'
        if votos_cand_3 > cand_mais_votos:
            cand_mais_votos = votos_cand_3
            candidato = f'{candidatos[2]} com {votos_cand_3} votos'
        if votos_cand_4 > cand_mais_votos:
            cand_mais_votos = votos_cand_4
            candidato = f'{candidatos[3]} com {votos_cand_4} votos'

    print(f'Total votos: {total_votos}x')

    while True:
        sair = input('Digite 0 para sair e \'sim\' para continuar: ').lower()
        if sair == 'sim' or sair == '0':
            break
        print('Entrada invalida! Digite \'0\' ou \'sim\'')

    if sair == '0':
        print('APURANDO ELEICAO PRISIDENCIAL...')
        sleep(1)
        break

percentagem_branco = (votos_branco * 100) / total_votos
print(percentagem_branco)

percentagem_nulo = (votos_nulo * 100) / total_votos
print(percentagem_nulo)

print('Total de Votos para cada Candidato:')
print('-' * 30)
print(f'Candidato {candidatos[0]} com {votos_cand_1} votos')
print(f'Candidato {candidatos[1]} com {votos_cand_2} votos')
print(f'Candidato {candidatos[2]} com {votos_cand_3} votos')
print(f'Candidato {candidatos[3]} com {votos_cand_4} votos')
print(f'Total de votos brancos : {votos_branco}')
print(f'Porcentagem de votos brancos sobre o total de votos: {percentagem_branco:.1f}%')
print(f'Total de votos nulos : {votos_nulo}')
print(f'Porcentagem de votos nulos sobre o total de votos: {percentagem_nulo:.1f}%')
print('-' * 30)
print(f'Candidato vencedor da eleicao: {candidato}')
print('-' * 30)
