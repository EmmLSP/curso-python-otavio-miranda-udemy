# Operador Lógico "and" 

# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if condicao: True
#    ...
# else: False
#    ...

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True and True)

# Avaliacao de curto circuito
print(True and False and True)

# retorna 0 - False para o Python
print(True and 0 and True)

# confrontar 0 0.0 '' com booleano
print(bool(0))
print(bool(0.0))
print(bool(''))
