"""
Exercicio 003
Faca um programa que calcule a soma entre todos
os numeros impares que sao multiplos de tres e
que se encontram no intervalo de 1 ate 500.
"""

soma = cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n

print(f'A soma de todos os {cont} valores solicitados é {soma}')
