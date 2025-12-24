"""
Exercicio 033
O Departamento Estadual de Meteorologia lhe contratou para 
desenvolver um programa que leia um conjunto indeterminado 
de temperaturas, e informe ao final a menor e a maior 
temperatura, bem como a media das temperaturas.
"""

temperaturas = int(input('Digite a quantidade de temperaturas: '))

maior = menor = soma_temp = media_temp = 0
for temp in range(temperaturas):
    temperatura = float(input(f'Digite a temperatura {temp + 1}: °C '))
    soma_temp += temperatura
    if temp == 0:
        menor = maior = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
media_temp = soma_temp / temperaturas

print(f'Menor temperatura: {menor:.1f}°C')
print(f'Maior temperatura: {maior:.1f}°C')
print(f'Media das temperaturas: {media_temp:.1f}°C')
