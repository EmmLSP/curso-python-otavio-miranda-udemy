"""
Exercicio 023
Faca um programa que mostre todos os primos entre 1 e N 
sendo N um numero inteiro fornecido pelo usuario. O 
programa devera mostrar tambem o numero de divisoes que 
ele executou para encontrar os numeros primos. Serao 
avaliados o funcionamento, o estilo e o numero de testes 
(divisoes) executadas.
"""

numeros = int(input('Digite os numeros primos dentro do intervalo de 1 e N: '))

print(f'\nNumeros PRIMOS entre 1 e {numeros}:')
print('-' * 30)

for num in range(2, numeros+1):
    primo = 0
    for n in range(1, num+1):
        if num % n == 0:
            primo += 1

    if primo == 2:
        for n in range(1, num+1):
            if num % n == 0:
                print(f'{num} é divisivel por {n}')
    if primo == 2:
        print('-' * 30)
