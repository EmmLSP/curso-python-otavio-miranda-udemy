"""
Exercicio 017
Faca um programa que calcule o fatorial de um
numero inteiro fornecido pelo usuario.
Ex.: 5!=5.4.3.2.1=120.

fat *= num
  1 =   1 * 5
  5 =   5 * 4
 20 =  20 * 3
 60 =  60 * 2
120 = 120 * 1
= 120
"""

num = int(input('Digite um numero para o fatorial: '))
fat = 1
print(f'{num}! = ', end='')
for n in range(num, 0, -1):
    fat *= n
    if n > 1:
        print(f'{n} x ', end='')
    else:
        print(f'{n} = ', end='')
    n -= 1

print(fat)
