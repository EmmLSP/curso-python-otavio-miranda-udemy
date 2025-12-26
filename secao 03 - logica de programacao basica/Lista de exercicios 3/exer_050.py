"""
Exercicio 050
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faca um programa 
que calcule o valor de H com N termos.
"""

termos = int(input('Digite n termos para formar uma serie 1/N: '))

print('H = 1 + ', end='')
valor_h = 1
for n in range(2, termos+1):
    valor_h += 1/n 
    print(f'1/{n} + ', end='')
print('... + 1/N.')
print(f'Valor de H: {valor_h:.2f}')
