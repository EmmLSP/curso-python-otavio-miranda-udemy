"""
Exercicio 021
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999, 
que e a condicao de parada. No final, mostre quantos numeros 
foram digitados e qual foi a soma entre eles (desconsiderando 
a flag).
"""

soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos {cont} valores foi {soma}!')
