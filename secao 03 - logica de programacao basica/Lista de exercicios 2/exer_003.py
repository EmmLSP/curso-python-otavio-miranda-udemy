"""
Exercicio 03
Faca um programa que verifique se uma letra digitada
é 'F' ou 'M'. Conforme a letra escrever: F-Feminino,
M-Masculino, Sexo invalido.
"""

sexo = input('Digite seu sexo [F/M]: ')
tamanho = len(sexo)
if sexo.isalpha():
    if tamanho == 1:
        if sexo == 'f' or sexo == 'F':
            print('F - Feminino')
        elif sexo == 'm' or sexo == 'M':
            print('M - Masculino')
        else:
            print('Sexo invalido!')
    else:
        print('Por favor, digite uma letra: "F" ou "M"')
else:
    print('Por favor, digite uma letra')


sexo = input('Digite seu sexo [F/M]: ').strip().upper()
tamanho = len(sexo)
if sexo.isalpha():
    if tamanho == 1:
        if sexo == 'F':
            print('F - Feminino')
        elif sexo == 'M':
            print('M - Masculino')
        else:
            print('Sexo invalido!')
    else:
        print('Por favor, digite uma letra: "F" ou "M"')
else:
    print('Por favor, digite uma letra')
