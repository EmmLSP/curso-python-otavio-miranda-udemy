"""
Exercicio 032
Faca um programa que calcule o fatorial de um numero
inteiro fornecido pelo usuario. Ex.: 5!=5.4.3.2.1=120.
A saida deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! = 5 . 4 . 3 . 2 . 1 = 120  
"""

num = int(input('Digite um numero para calcular o fatorial: '))
fat = 1
i = num
print(f'Fatorial de: {num}')
fatorial = f'{num}! = '
while i > 0:
    fat *= i
    if i > 1:
        fatorial += f'{i} . '
    else:
        fatorial += f'{i} = {fat}\n' 
    i -= 1

print(fatorial)
