"""
Exercicio 016
A serie de Fibonacci é formada pela sequencia
1, 1, 2, 3, 5, 8, 13, 21, 34, 55,... Faca um
programa que gere a serie ate que o valor seja
maior que 500.
"""

anterior = 1
atual = 1
posterior = 0 # inicializar a variavel

print('1, 1, ', end='')
while posterior < 500:
    posterior = anterior + atual
    anterior = atual
    atual = posterior
    if posterior < 500:
        print(f'{posterior}, ', end='')
    else:
        print(f'{posterior}')
