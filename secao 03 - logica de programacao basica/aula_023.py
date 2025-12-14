# Operador lógico "not"

# Operador logico "not"
# Usado para inverter expressoes
# not True = False
# not False = True
# string vazia "" - False

print('not True  :', not True)
print('not False :', not False)
print('not 0     :', not 0)
print('not 1     :', not 1)
print('not 0.0   :', not 0.0)
print('not 0.1   :', not 0.1)
print('not ""    :', not '')
print('not "abc" :', not 'abc')

senha = input('Senha: ')

# not "" -> not False -> True
if not senha:
    print('Voce nao digitou nada')

