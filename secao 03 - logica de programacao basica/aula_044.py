# range + for para usar intervalos de números

"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(10)
print(numeros)
numeros = range(5, 10)
print(numeros)
numeros = range(5, 10, 2)
print(numeros)
print()

# ultimo digito nao e incluido
numeros = range(10)
for numero in numeros:
    print(numero)
print()

numeros = range(5, 10)
for numero in numeros:
    print(numero)
print()

numeros = range(2, 20, 2)
for par in numeros:
    print(par)
print()

numeros = range(1, 20, 2)
for impar in numeros:
    print(impar)
print()

numeros = range(10, 0, -1)
for num_decresc in numeros:
    print(num_decresc)
print()

numeros = range(0, 100, 8)
for multiplos_8 in numeros:
    print(multiplos_8)
print()

# ignora o ultimo valor: -10
numeros = range(0, -10, -1)
for num_negativos in numeros:
    print(num_negativos)
print()

numeros = range(0, -20, -2)
for num_negativos in numeros:
    print(num_negativos)
print()

nomes = ['Pedro', 'Maria', 'Joao', 'Amanda', 'Anna']
for nome in nomes:
    print(nome)
print()

vogais = 'aeiou'
for letra in vogais:
    print(letra)
print()
