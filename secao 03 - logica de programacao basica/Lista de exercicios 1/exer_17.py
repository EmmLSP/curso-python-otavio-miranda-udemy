"""
Exercicio 17
Faca um programa que peca a temperatura em graus 
Celsius, transforme e mostre em graus Farenheit.

F = (C * 9/5) + 32
"""

celsius_str = input('Digite a temperatura em graus °C para °F: ')
celsius = float(celsius_str)
farenheit = (celsius * 9/5) + 32
print(f'A temperatura de {celsius:.1f}°C, convertido para farenheit é {farenheit:.1f}°F')
