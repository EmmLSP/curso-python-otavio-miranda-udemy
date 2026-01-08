"""
Exercicio 08
Escreva um programa que leia um valor em metros e 
o exiba convertido em km, hm, dam, m, dm, cm, mm
"""

metro_str = input('Uma distancia em metros: ')
metro = float(metro_str)
km = metro / 1000
hm = metro / 100
dam = metro / 10
m = metro * 1
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'\nA medida de {metro}m corresponde a:\n')
print('  Tabela de Conversao entre km, hm, dam, m, dm, cm, mm')
print('-' * 60)
print('Unidade              Simbolo         Equivalencia em metros')
print('-' * 60)
print(f'Quilometro           km              {metro}m = {km}km')
print(f'Hectometro           hm              {metro}m = {hm}hm')
print(f'Decametro            dam             {metro}m = {dam}dam')
print(f'Metro                m               {metro}m = {m:.0f}m')
print(f'Decimetro            dm              {metro}m = {dm:.0f}dm')
print(f'Centimetro           cm              {metro}m = {cm:.0f}cm')
print(f'Milimetro            mm              {metro}m = {mm:.0f}mm')
print('-' * 60)
