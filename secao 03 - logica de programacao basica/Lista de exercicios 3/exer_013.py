"""
Exercicio 013
Faca um programa que peca dois numeros, base e expoente,
calcule e mostre o primeiro numero elevado ao segundo 
numero. Não utilize a funcao de potencia da linguagem.

Ex: 
pot = 1
2 ^ 3 = 8 
base x base x base = 2 x 2 x 2

pot *= base (1 *= 2 == 2)
pot *= base (2 *= 2 == 4)
pot *= base (4 *= 2 == 8)
"""

base = float(input('Digite um numero para elevar a potencia: '))
expoente = int(input('Digite o expoente de potencia: '))
pot = 1
for n in range(expoente):
    pot *= base

print(f'{base} ** {expoente} = {base ** expoente}')
print(f'{base} ** {expoente} = {pot}')
