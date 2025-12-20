# Exercício guiado - Calculadora - versao 1

# Calculadora com while

from time import sleep
from os import system

while True:
    resultado = 0
    print('-' * 15)

    numero_1 = input('Digite primeiro numero: ')
    numero_2 = input('Digite segundo numero: ')
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        system('cls')
        print('Erro: Tipo de dado invalido!')
        continue

    print('[ + ] SOMA')
    print('[ - ] SUBTRACAO')
    print('[ / ] DIVSAO')
    print('[ * ] MULTIPLICACAO')
    oper = input('Digite o operador: ')

    if len(oper) > 1:
        system('cls')
        print('Mais de um operador.')
        continue
   
    if oper not in '+-/*':
        system('cls')
        print('Operador inválido!')
        continue

    if oper == '+':
        resultado = num_1_float + num_2_float
    elif oper == '-':
        resultado = num_1_float - num_2_float
    elif oper == '/':
        resultado = num_1_float / num_2_float
    elif oper == '*':
        resultado = num_1_float * num_2_float

    print('-' * 15)
    print(f'Resultado: {num_1_float} {oper} {num_2_float} = {resultado}')
    print('-' * 15)

    while True:
        resp = input('Quer sair? [S]im [N]ao: ').lower()[0]
        if resp not in 'sn':
            system('cls')
            print('-' * 15)
            print('Para continuar digite N e para sair digite S')
            continue
        break

    if resp.startswith('s'):
        system('cls')
        print('ENCERRANDO...')
        sleep(1)
        break

system('cls')
print('\n<<< FIM DO PROGRAMA >>>\n')
