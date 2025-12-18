"""
Exercicio 05
Faca um programa para a leitura de duas notas
parciais de um aluno. O programa deve calcular
a media alcancada pelo aluno e apresenta:
- A mensagem 'Aprovado', se a media alcancada 
for maior ou igual a sete.
- A mensagem 'Recuperacao', se a media for menor
que sete e maior ou igual a 4.
- A mensagem 'Reprovado', se a media for menor
do que sete.
"""

nota1 = float(input('Digite nota1: '))
nota2 = float(input('Digite nota2: '))
media = (nota1 + nota2) / 2
print(f'Media: {media:.2f}')
if media >= 7:
    print('Aprovado')
elif media >= 4:
    print('Recuperacao')
else:
    print('Reprovado')
