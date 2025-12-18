"""
Exercicio 04
Faca um programa que verifique se uma letra 
é vogal ou consoante.
"""

letra = input('Digite uma letra: ').strip()
tam = len(letra)
if letra.isalpha() and tam == 1:
    if letra.lower() in 'aeiouáéíóú':
        print('É uma VOGAL')
    else:
        print('É uma CONSOANTE')
else:
    print('Não é uma letra')
