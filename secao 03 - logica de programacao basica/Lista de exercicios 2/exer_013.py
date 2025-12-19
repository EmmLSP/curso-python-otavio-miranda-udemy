"""
Exercicio 013
Faca um programa que leia um numero e exiba o dia 
correspondente da semana de 1 ate 7, se digitar 
outro valor deve aparecer valor invalido.
"""

print('-' * 42)
print(f'{'DIAS DA SEMANA':^42}')
print('-' * 42)
print('''| 1 - Domingo       | 2 - Segunda-Feira  |
| 3 - Terca-Feira   | 4 - Quarta-Feira   |
| 5 - Quinta-Feira  | 6 - Sexta-Feira    |
| 7 - Sábado                             |''')
print('-' * 42)
dia = int(input('Digite o dia da semana de acordo com os valores acima: '))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-Feira')
elif dia == 3:
    print('Terca-Feira')
elif dia == 4:
    print('Quarta-Feira')
elif dia == 5:
    print('Quinta-Feira')
elif dia == 6:
    print('Sexta-Feira')
elif dia == 7:
    print('Sabado')
else:
    print('Valor invalido!')
