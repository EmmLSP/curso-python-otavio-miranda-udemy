"""
Exercicio 018 2
Crie um programa que leia nome e duas notas de
varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de
cada um e permita que o usuario possa mostrar as
notas de cada aluno individualmente.
"""

from time import sleep

ficha = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 24)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-=' * 30)

while True:
    opc = int(input('Mostrar notas e resultado de qual aluno? (999 interrompe): '))
    
    if opc == 999:
        print('Finalizando...')
        sleep(1)
        break
    
    if 0 > opc or opc > len(ficha) - 1:
        continue
    
    print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]} - ', end='')
    if ficha[opc][2] >= 7:
        print('\033[32mAPROVADO\033[m')
    elif ficha[opc][2] >= 5:
        print('\033[33mRECUPERACAO\033[m')
    else:
        print('\033[31mREPROVADO\033[m')

print('<<< VOLTE SEMPRE >>>')
