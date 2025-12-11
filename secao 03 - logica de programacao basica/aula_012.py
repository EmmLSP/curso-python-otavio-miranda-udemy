# Exercicio 02 - Calculo do IMC (Indice de Massa Corporea) + Ellipsis

nome = 'Luiz Otavio'
altura = 1.80 # metros
peso = 95 # kg
imc = peso / (altura ** 2)
 
# imc = ... -> Ellipsis, placeholder

# IMC = peso / (altura x altura)
# peso em kg
# altura em metros 

# Luiz Otavio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

print(nome, 'tem', '{:.2f}'.format(altura), 'de altura,')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)
print(...)