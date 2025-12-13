"""
Exercicio 16
Faca um programa que peca a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius.

C = 5/9 * (F - 32)
"""

farenheit_str = input('Digite a temperatura em graus °F para °C: ')
farenheit = float(farenheit_str)
celsius1 = (farenheit - 32) * 5/9
celsius2 = 5/9 * (farenheit - 32)
print(f'A temperatura de {farenheit}°F convertida em celsius é {celsius1:.1f}°C')
print(f'A temperatura de {farenheit}°F convertida em celsius é {celsius2:.1f}°C')
