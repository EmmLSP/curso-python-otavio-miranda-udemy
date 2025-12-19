"""
Exercicio 038
Crie um programa que leia duas notas de um aluno e 
calcule sua media, mostrando uma mensagem no final, 
de acordo com a media atingida:

- Media abaixo de 5.0:
"REPROVADO"
- Media entre 5.0 e 6.9:
"RECUPERACAO"
- Media 7.0 ou superior:
"APROVADO"
"""

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'Tirando {nota_1:.1f} e {nota_2:.1f}, a media do aluno é {media:.1f}')
print('O aluno esta ', end='')
if media >= 7.0:
    print('APROVADO.')
elif media >= 5.0:
    print('em RECUPERACAO.')
else:
    print('REPROVADO.')
