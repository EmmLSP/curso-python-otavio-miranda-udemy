# Introdução ao empacotamento e desempacotamento

"""
Introducao ao desempacotamento + tuples (tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

# nome1, nome2 = ['Maria', 'Helena', 'Luiz']
# print(nome2)
# ValueError: too many values to unpack

# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz']
# print(nome2)
# ValueError: not enough values to unpack

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

# *resto -> *_

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)

_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome, _)
