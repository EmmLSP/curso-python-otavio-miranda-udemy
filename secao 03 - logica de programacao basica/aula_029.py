# Introdução ao try e except para capturar erros (exceptions)

"""
Introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
input() -> sempre retorna uma string
"""

# 1 print(123) o Python leu esta linha depois
# 2 print(456) o Python leu a linha de baixo
# quando chegou na 3 linha deu um erro,
# ocorreu uma exceção, except
# 3 int('a')
# ValueError: invalid literal for int() with base 10: 'a'
# try except -> capturar os erros do usuario

numero_str = input('Vou dobrar o nnumero que voce digitar: ')

try:
    print(numero_str, type(numero_str))
    numero_float = float(numero_str)
    print(numero_float, type(numero_float))

    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso nao é um numero')

try:
    ...
except:
    ...

try:
    pass
except:
    pass

# sempre precisa tratar o input do usuario
# isdigit() -> checa se usuario digitou apenas numeros

# 1 versao
numero_str = input('Vou dobrar o nnumero que voce digitar: ')
# checar se string e um numero inteiro, float nao funciona
if numero_str.isdigit():
    # tratar entrada do usuario, converter str para float
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print(f'Isso nao e um numero')

# 2 versao
numero_str = input('Vou dobrar o nnumero que voce digitar: ')
# checar se string é um numero or substituir . por ''
if numero_str.isdigit() or numero_str.replace('.', ''):
    # tratar entrada do usuario, converter str para float
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print(f'Isso nao e um numero')
