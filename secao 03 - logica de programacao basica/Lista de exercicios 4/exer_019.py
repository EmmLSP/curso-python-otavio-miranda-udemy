"""
Exercicio 019
Crie um programa que leia varios numeros inteiros pelo
teclado. O programa so vai parar quando o usuario digitar
o valor 999, que é condicao de parada (flag). No final, 
mostre quantos numeros foram digitados e qual foi a soma
entre eles (desconsiderando a flag).
"""

num = cont = soma = 0
numeros = ''
while num != 999:
    num = int(input('Digite um numero [999 para parar]:  '))
    if num != 999:
        numeros += f'{num} '
        soma += num # acumulador
        cont += 1 # contador

print(f'Numeros digitados: {numeros}')
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')
