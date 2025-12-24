"""
Exercicio 037
Uma academia deseja fazer um senso entre seus clientes para 
descobrir o mais alto, o mais baixo, o mais gordo e o mais 
magro, para isto voce deve fazer um programa que pergunte a 
cada um dos clientes da academia seu codigo, altura e seu 
peso. O final da digitacao de dados deve ser dada quando o 
usuario digitar 0 (zero) no campo codigo. Ao encerrar o 
programa tambem devem ser informados os codigos e valores do 
cliente mais alto, do mais baixo, do mais gordo e do mais 
magro, alem da media das alturas e dos pesos dos clientes.
"""

clientes = 1
mais_alto = mais_baixo = mais_gordo = mais_magro = 0
media_altura = media_peso = soma_altura = soma_peso = 0
cod_alto = cod_baixo = cod_gordo = cod_magro = ''
while True:
    codigo = int(input(f'Digite o codigo do cliente {clientes} ou digite 0 zero para encerrar: '))
    if codigo == 0:
        break
    altura = float(input('Digite a altura: (m) '))
    peso = float(input('Digite a peso: (Kg) '))

    if clientes == 1:
        cod_alto = cod_baixo = cod_gordo = cod_magro = f'cliente {clientes} codigo {codigo}'
        mais_alto = mais_baixo = altura
        mais_gordo = mais_magro = peso
    else:
        if altura > mais_alto:
            mais_alto = altura
            cod_alto = f'cliente {clientes} codigo {codigo}'
        if altura < mais_baixo:
            mais_baixo = altura
            cod_baixo = f'cliente {clientes} codigo {codigo}'
    
        if peso > mais_gordo:
            mais_gordo = peso
            cod_gordo = f'cliente {clientes} codigo {codigo}'
        if peso < mais_magro:
            mais_magro = peso
            cod_magro = f'cliente {clientes} codigo {codigo}'
    soma_altura += altura
    soma_peso += peso
    clientes += 1

media_altura = soma_altura / clientes
media_peso = soma_peso / clientes

if clientes > 0:
    print('-' * 30)
    print(f'Mais gordo - {cod_gordo} com {mais_gordo} Kg')
    print(f'Mais magro - {cod_magro} com {mais_magro} Kg')
    print(f'Mais alto  - {cod_alto} com {mais_alto} m')
    print(f'Mais baixo - {cod_baixo} com {mais_baixo} m')
    print('-' * 30)
    print(f'Media das alturas dos clientes: {media_altura:.2f} m')
    print(f'Media dos pesos dos clientes: {media_peso:.1f} Kg')
    print('-' * 30)
else:
    print('O censo nao foi realizado com nenhum cliente!')
