# id - A identidade do valor que está na memória

"""
Flag (Bandeira) - Marcar um local
None - nao valor
is e is not = é ou nao é (tipo, valor, identidade)
id = Identidade
"""

# as 2 variaveis estao apontando para
# o mesmo lugar na memoria

v1 = 'a'
v2 = 'a'

# 140704508178400
print(id(v1))
# 140704508178400
print(id(v2))

# as 2 variaveis estao apontando para
# lugares diferentes na memoria

v3 = 'a'
v4 = 'b'

# 140704520630240
print(id(v3))
# 140704520630288
print(id(v4))
