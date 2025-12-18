"""
Exercicio 22
Faca um programa que faca 5 perguntas para uma pessoa
sobre um crime. As perguntas sao:
1. Telefoneu para a vitima?
2. Esteve no local do crime?
3. Mora perto da vitima?
4. Devia para a vitima?
5. Ja trabalhou com a vitima?
O programa deve no final emitir uma classificacao sobre
a partiticipacao da pessoa no crime. Se a pessoa responder
positivamente a 2 questoes ela deve ser classificada como
suspeita, entre 3 e 4 como cumplice e 5 como assissano.
Caso contrario, sera classificado como inocente.
"""

cont = 0
resp1 = input('Telefoneu para a vitima? ').upper()
if resp1 == 'S':
    cont += 1

resp2 = input('Esteve no local do crime? ').upper()
if resp2 == 'S':
    cont += 1

resp3 = input('Mora perto da vitima? ').upper()
if resp3 == 'S':
    cont += 1

resp4 = input('Devia para a vitima? ').upper()
if resp4 == 'S':
    cont += 1

resp5 = input('Ja trabalhou com a vitima? ').upper()
if resp5 == 'S':
    cont += 1

if cont < 2:
    print('Inocente')
elif cont == 2:
    print('Suspeita')
elif cont == 3 or cont == 4:
    print('Cumplice')
else:
    print('Assassino')
