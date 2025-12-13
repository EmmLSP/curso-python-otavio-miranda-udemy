"""
Exercicio 20
Faca um programa que peca 2 numeros inteiros e um
numero real. 
Calcule e mostre:
a. O produto do dobro do primeiro com metade do segundo.
b. A soma do triplo do primeiro com o terceiro.
c. O terceiro elevado ao cubo. 
"""

num1_int_str = input('Digite um numero inteiro: ')
num1_int = int(num1_int_str)
num2_int_str = input('Digite outro numero inteiro: ')
num2_int = int(num2_int_str)
num_float_str = input('Digite um numero real: ')
num_float = float(num_float_str)
res1 = (num1_int * 2) * (num2_int / 2)
res2 = (num1_int * 3) + num_float
res3 = num_float ** 3 # 2 elevado ao cubo
print(f'O produto do dobro do {num1_int} com metade de {num2_int} é {res1}')
print(f'A soma do triplo de {num1_int} com o {num_float} é {res2}')
print(f'{num_float} elevado ao cubo é {res3}')
