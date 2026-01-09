"""
Exercicio 006
Crie um programa que tenha uma tupla com varias
palavras (nao usar acentos). Depois disso, voce
deve mostrar, para cada palavra, quais sao as 
suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python',
    'curso', 'grátis', 'estudar', 'praticar', 'trabalhar',
    'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiouáàãéíóòõú':
            print(f'{letra} ', end='')
    print()
