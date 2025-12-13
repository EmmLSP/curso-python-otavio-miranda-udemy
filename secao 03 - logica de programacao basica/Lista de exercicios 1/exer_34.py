"""
Exercicio 34
Faca um programa que leia uma frase pelo
teclado e mostre:

- Quantas vezes aparece a letra "A".
- Em que posicao ela aparece pela primeira vez.
- Em que posicao ela aparece pela ultima vez.
"""

frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.upper().count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posicao {frase.find('A') + 1}')
print(f'A ultima letra A apareceu na posicao {frase.rfind('A') + 1}')
