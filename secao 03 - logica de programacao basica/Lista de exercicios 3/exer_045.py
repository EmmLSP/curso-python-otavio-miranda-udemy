"""
Exercicio 045
Desenvolver um programa para verificar a nota do aluno 
em uma prova com 10 questoes, o programa deve perguntar 
ao aluno a resposta de cada questao e ao final comparar 
com o gabarito da prova e assim calcular o total de acertos 
e a nota (atribuir 1 ponto por resposta certa). Apos cada 
aluno utilizar o sistema deve ser feita uma pergunta se 
outro aluno vai utilizar o sistema. Apos todos os alunos 
terem respondido informar:
- Maior e menor acerto
- Total de alunos que utilizaram o sistema
- A media das notas da turma

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Apos concluir isto voce poderia incrementar o programa
permitindo que o professor digite o gabarito da prova
antes dos alunos usarem o programa.
"""

print('Preencha o gabarito com dez notas:')
gabarito = ['', '', '', '', '', '', '', '', '', '']
for n in range(len(gabarito)):
    gabarito[n] = input(f'Digite a nota da questao {n + 1}: ').upper()

print('Gabarito da Prova:')
for nota in range(len(gabarito)):
    print(f'{nota+1:02} - {gabarito[nota]}')
print()

qtd_alunos = 0
num_aluno = 0
maior_acerto = menor_acerto = soma_media_turma = 0
aluno_maior = aluno_menor = i = 0
while True:  
    nota_aluno = []
    media_aluno = 0
    total_notas = 0
    questoes = 1
    notas_aluno_str = ''
    num_aluno += 1
    print(f'Aluno {num_aluno}:')
    print('-' * 15)
    acertos = 0
    for n in range(len(gabarito)):
        while True:
            nota = input(f'Digite a resposta da questao {questoes}: ').upper()
            if nota in 'ABCDE':
                break
            print('LETRA ERRADA! Digite \'A\', \'B\', \'C\', \'D\' ou \'E\'')
        nota_aluno.append(nota)
        questoes += 1

        if nota_aluno[n] == gabarito[n]:
            notas_aluno_str += f'\033[32m{nota}\033[m '
            total_notas += 1
            acertos += 1
        else:
            notas_aluno_str += f'\033[31m{nota}\033[m '
  
    if i == 0:
        maior_acerto = menor_acerto = acertos
        aluno_maior = aluno_menor = num_aluno
    else:
        if acertos > maior_acerto:
            maior_acerto = acertos
            aluno_maior = num_aluno
        if acertos < menor_acerto:
            menor_acerto = acertos
            aluno_menor = num_aluno

    media_aluno = (total_notas * 10) / len(gabarito)
    soma_media_turma += media_aluno

    print(f'Aluno {qtd_alunos + 1}:')
    
    print(f'Notas: {notas_aluno_str}')

    print(f'Media = {media_aluno:.1f} - ', end='')

    if media_aluno >= 7:
        print('APROVADO')
    elif media_aluno >= 5:
        print('RECUPERACAO')
    else:
        print('REPROVADO')

    while True:
        continuar = input('Digite \'S\' para continuar ou \'N\' para sair: ').upper()
        if continuar not in 'SN':
            print('Entrada invalida! Digite \'S\' ou \'N\'')
            continue
        break
    
    i += 1
    qtd_alunos += 1

    if continuar == 'N':
        break

media_turma = soma_media_turma / qtd_alunos

print('-' * 30)
print(f'O aluno {aluno_maior} teve maior quantidades de acertos com {maior_acerto} no total')
print(f'O aluno {aluno_menor} teve menor quantidades de acertos com {menor_acerto} no total')
print(f'O sistema foi utilizado por {qtd_alunos} alunos')
print(f'A media de notas da turma é {media_turma:.1f}')
