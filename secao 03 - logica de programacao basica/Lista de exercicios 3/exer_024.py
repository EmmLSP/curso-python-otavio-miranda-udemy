"""
Exercicio 024
Faca um programa que calcule e mostre a media
aritmetica de N notas.
"""

qtd_notas = int(input('Digite a quantidade de notas: '))
seq_notas = ''
i = soma = media = 0
while i < qtd_notas:
    nota = float(input(f'Digite a nota {i + 1}: '))
    soma += nota
    if i < qtd_notas - 1:
        seq_notas += f'{nota:.1f}, '
    else:
        seq_notas += f'{nota:.1f}'
    i += 1

media = soma / qtd_notas
print(f'Notas: {seq_notas}')
print(f'Soma = {soma}')
print(f'Media = {media:.1f}')
