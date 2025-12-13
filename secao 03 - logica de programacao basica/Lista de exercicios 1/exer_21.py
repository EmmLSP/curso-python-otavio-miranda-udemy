"""
Exercicio 21
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte formula: (72.7 * altura) - 58
"""

altura_str = input('Digite a altura: ')
altura = float(altura_str)
peso_ideal = (72.7 * altura) - 58
print(f'O peso ideal para altura de {altura}m é de {peso_ideal:.2f} kg')
