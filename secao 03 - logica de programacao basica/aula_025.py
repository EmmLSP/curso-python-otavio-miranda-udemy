# Interpolação de string com % em Python

# Interpolacao basica de strings
# s - string
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

# colocar os placeholder: %d, %.2f depois de % as variveis
nome = 'Luiz'
preco = 1000.958943
variavel = '%s o preco é R$%.2f\n' % (nome, preco)
print(variavel, end='')

# converter 15 para hexadecimal
print('O hexadecimal de %d é %04x' % (15, 15))
print('O hexadecimal de %d é %04X' % (15, 15))
print('O hexadecimal de %d é %04x' % (150, 150))
print('O hexadecimal de %d é %04X' % (150, 150))
print('O hexadecimal de %d é %04x' % (1500, 1500))
print('O hexadecimal de %d é %04X' % (1500, 1500))
