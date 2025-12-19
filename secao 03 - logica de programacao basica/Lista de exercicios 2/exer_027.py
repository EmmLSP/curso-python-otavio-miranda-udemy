"""
Exercicio 027
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo 
que ele foi multado. 
A multa vai custar R$7.00 por km acima do limite.
"""

velocidade = int(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\033[1;31mMULTADO! Voce excedeu o limite permitido que é de 80 km/h')
    print(f'Voce deve pagar uma multa de \033[mR${multa:.2f}!')
else:
    print('\033[1;32mVelocidade dentro do limite de 80km/h.\033[m')
if velocidade <= 80:
    print('\033[1;32mTenha um bom Dia! Dirija com seguranca!\033[m')
else:
    print('\033[1;33mTenha um bom Dia! Dirija com mais cuidado!\033[m')
