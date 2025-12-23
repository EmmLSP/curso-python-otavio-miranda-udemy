"""
Exercicio 025
Faca um programa que peca para n pessoas a sua
idade, ao final o programa devera verificar se
a media de idade da turma varia entre 0 e 25,
26 e 60 e maior que 60, e entao, dizer se a 
turma é jovem, adulta ou idosa, coforme a media
calculada.
"""

pessoas = int(input('Digite a quantidade de pessoas: '))

soma = media = 0
for n in range(pessoas):
    idade = int(input(f'Digite a idade da pessoa {n + 1}: '))
    soma += idade
media = soma / pessoas
print(f'A media da turma é de {media:.1f} anos', end='')
if 0 <= media <= 25:
    print(' - Turma Jovem!')
elif 25 < media <= 60:
    print(' - Turma Adulta!')
else: 
    print(' - Turma Idosa!')
