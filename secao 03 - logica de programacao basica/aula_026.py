# Formatação de strings com f-strings

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a -> chama metodo -> __repr__ __str__ 
"""

# no Python tem bibliotecas para formacao
# de datas, precos, numeros

variavel = 'ABC'
print(f'{variavel}.')
print(f'{variavel:>10}.') # 10 caracteres para esquerda
print(f'{variavel:<10}.') # 10 caracteres para direita
print('-' * 15)
print(f'{variavel:^10}.') # 10 caracteres centralizado
print(f'{variavel:$^10}.')
print(f'{variavel:#^10}.')
print(f'{variavel:-^10}.')
print(f'{variavel:=^10}.')
print(f'{variavel:@^10}.')
print('-' * 15)
print(f'{1000.487952:.1f}')
print(f'{1000.487952:,.1f}')
print(f'{1000.487952:+,.1f}')
print(f'{-1000.487952:+,.1f}')
print(f'{1000.487952:-,.1f}')
print(f'{-1000.487952:-,.1f}')
print(f'{1000.487952:0=+10,.1f}')
print(f'{1000.487952:0=+15,.1f}')
print(f'{1000.487952:0=+15,.2f}')
print('-' * 15)
print('O hexadecimal de %d é %04x' % (1500, 1500)) # com interpolacao
print('O hexadecimal de %d é %08x' % (1500, 1500)) # com interpolacao
print(f'O hexadecimal de 1500 é {1500:04x}') # com f-strings
print(f'O hexadecimal de 1500 é {1500:08x}') # com f-strings
print(f'O hexadecimal de 1500 é {1500:04X}') # com f-strings
print(f'O hexadecimal de 1500 é {1500:08X}') # com f-strings
print('-' * 15)
# opcional, pode tirar se vier em algum codigo, 
# os metodos !r !s !a
print(f'{variavel!r}') # __repr__
print(f'{variavel!s}') # __str__
print(f'{variavel!a}') # __ascii__
