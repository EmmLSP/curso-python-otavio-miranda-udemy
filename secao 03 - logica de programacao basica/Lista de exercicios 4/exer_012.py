"""
Exercicio 012
Faca um programa que leia o sexo de uma pessoa,
mas so aceite os valores 'M' ou 'F'. Caso esteja
errado, peca a digitacao novamente ate ter um
valor correto.
"""

sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('\033[1;31mDados invalidos. por favor, informe seu sexo:\033[m ').upper().strip()[0]
# sexo = 'Masculino' if sexo == 'M' else 'Feminino'
print(f'\033[1;32mSexo \'{sexo}\' registrado com sucesso!\033[m')
