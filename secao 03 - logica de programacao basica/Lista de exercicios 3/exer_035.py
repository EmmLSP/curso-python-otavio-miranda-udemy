"""
Exercicio 035
Encontrar numeros primos e uma tarefa dificil. Faca um 
programa que gera uma lista de numeros primos existentes 
entre 1 e um numero inteiro informado pelo usuario.
"""

num = int(input('Digite um numero: '))
print(f'Numero Primos de 1 ate {num}:')
print('-' * 30)
i = 1
while i <= num:
    if i < 2:
        # print(f'{i} NAO é PRIMO')
        i += 1
        continue  
    primo = 0
    for n in range(1, i+1):
        if i % n == 0:
            primo += 1
    if primo == 2:
        print(f'{i} ', end='')
    i += 1
