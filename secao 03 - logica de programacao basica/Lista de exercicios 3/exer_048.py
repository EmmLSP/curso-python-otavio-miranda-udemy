"""
Exercicio 048
Faca um programa que peca um numero inteiro positivo
e em seguida mostre este numero invertido:
Exemplo:
123456789
=> 987654321
"""

numeros = input('Digite um numero: ')
numeros_int = []
for n in range(len(numeros)):
    numeros_int.append(int(numeros[n]))

for n in range(len(numeros) // 2):
    valor_temp = numeros_int[n]
    numeros_int[n] = numeros_int[len(numeros) - 1 - n]
    numeros_int[len(numeros) - 1 - n] = valor_temp

print(numeros)
print('=> ', end='')
for num in numeros_int:
    print(num, end='')
print()
