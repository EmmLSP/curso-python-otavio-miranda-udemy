"""
Exercicio 001
Faca um programa que peca uma nota, entre zero e dez. Mostre 
uma mensagem caso o valor seja invalido e continue pedindo ate 
o usuario informe um valor valido.
"""

while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))
    if 0 <= nota <= 10:
        break
    print('Valor invalido! Nota precisa ser entre 0 e 10')

print(f'Valor de nota valida: {nota}')
