"""
Exercicio 027
Faca um programa que calcule o numero medio de
alunos por turma. Para isto, peca a quantidade
de turmas e a quantidade de alunos para cada 
turma. As turmas nao podem ter mais de 40 alunos.
"""

turmas = int(input('Digite a quantidade de turmas: '))

soma = media = 0
for n in range(turmas):
    while True:
        alunos = int(input(f'Digite a quantidade de alunos da turma {n + 1}: '))
        if alunos < 0 or alunos > 40:
            print('As turmas nao podem ter mais de 40 alunos')
            continue
        break
    soma += alunos
    media = soma / turmas

print(f'A media de alunos por turma é {media:.1f} alunos')
