"""
Exercicio 14
Faca um programa que le as duas notas parciais obtidas 
por um aluno numa disciplina ao longo  de um semestre, 
e calcule a sua media. A atribuicao de conceitos obedece 
a tabela abaixo:

Media de Aproveitamento         Conceito
-----------------------------------------
Entre 9.0 e 10.0                A
Entre 7.5 e 9.0                 B
Entre 6.0 e 7.5                 C
Entre 4.0 e 6.0                 D
Entre 4.0 e 0.0                 E
-----------------------------------------
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
conceito = ''
if 9.0 <= media <= 10:
    conceito = 'A'
elif 7.5 <= media < 9.0:
    conceito = 'B'
elif 6.0 <= media < 7.5:
    conceito = 'C'
elif 4.0 <= media < 6.0:
    conceito = 'D'
else:
    conceito = 'E'

print(f'Notas: {nota1:.1f} - {nota2:.1f}')
print(f'Conceito: {conceito}')
print(f'Media: {media:.1f} - ', end='')
if conceito == 'A' or conceito == 'B':
    print('Aprovado')
elif conceito == 'C' or conceito == 'D':
    print('Recuperacao')
else:
    print('Reprovado')
