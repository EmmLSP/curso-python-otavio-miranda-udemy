"""
Exercicio 034
Os numeros primos possuem varias aplicacoes dentro da
computacao, por exemplo na criptografia. Um numero primo
e aquele que é divisivel apenas por um e por ele mesmo.
Faca um programa que peca um numero inteiro e determine
se ele é ou nao um numero primo.
"""

num = int(input('Digite um numero: '))
primo = True
if num < 2:
    primo = False
i = 2
while i < num:
    if num % i == 0:
        # print(num, 'divisivel por', i)
        primo = False
        break
    i += 1
        
print(f'{num} é PRIMO' if primo else f'{num} NAO e PRIMO')
