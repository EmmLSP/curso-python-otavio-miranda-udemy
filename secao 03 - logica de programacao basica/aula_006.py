# conversao de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutaveis e primitivos:
# str, int, float, bool

# + -> polimorfismo, utilizando o mesmo 
# operador para fazer coisas diferentes 

print(1 + 1)
print('a' + 'b')

# TypeError: can only concatenate str (not "type") to str
# print('1' + 1)
#  coersao de str para int, retorna int
print(int('1') + 1) 

print('1', type('1'))
# int() -> coersao de tipo, conversao de tipo
print(int('1'), type(int('1'))) 

# coersao de str para float, retorna float
print(float('1') + 1)
# funcao type(), retorna tipo do retorno da coersao de str para float
print(type(float('1') + 1)) 

# string vazia, retorna False
print(bool('')) 
# string com espaco, retorna True
print(bool(' '))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(11 + 'b')
# coercao de int para str
print(str(11) + 'b')
