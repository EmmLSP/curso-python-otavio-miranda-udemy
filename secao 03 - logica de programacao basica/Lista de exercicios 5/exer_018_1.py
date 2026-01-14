"""
Exercicio 018 1
Crie um programa que leia nome e duas notas de
varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de
cada um e permita que o usuario possa mostrar as
notas de cada aluno individualmente.
"""

from time import sleep

alunos = []
aluno = []
notas = []
while True:
    aluno.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    soma = 0
    for c in range(len(notas)):
        soma += notas[c]
    media = soma / len(notas)
    aluno.append(media)
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()

    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp in 'SN':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    if resp == 'N':
        break

print('-=' * 30)
print(f'{'No.':<4}{'NOME':<15}{'MEDIA':>6}')
print('-' * 30)
for pos, aluno in enumerate(alunos):
    print(f'{pos:<4}{aluno[0]:<15}{aluno[2]:>6.1f}')

print('-' * 45)
while True:
    notas = int(input('Mostrar notas e status de qual aluno? (999 para sair): '))
    if 0 <= notas < len(alunos): 
        print(f'Notas de {alunos[notas][0]} sao {alunos[notas][1]} - ', end='')
        media = alunos[notas][2]
        if media >= 7:
            print('APROVADO')
        elif media >= 5:
            print('RECUPERACAO')
        else:
            print('REPROVADO')
    if notas == 999:
        print('Finalizando...')
        sleep(1)
        break

print('-=' * 30)
print('<<< VOLTE SEMPRE >>>')
