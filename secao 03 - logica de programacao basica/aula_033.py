# Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string
# tipos built-in, embutido, que vem dentro do Python
# str, int, float, bool sao objetos, possuem metodos, acoes 

"""
Documentacao Python -> Tipos de Dados
https://docs.python.org/3.14/library/datatypes.html
Documentacao Python -> Built-in Types
https://docs.python.org/3.14/library/stdtypes.html#text-sequence-type-str
Imutaveis que vistos ate agora: str, int, float, bool
"""

# capitalize() Retorna uma cópia da string com o seu primeiro 
# caractere em maiúsculo e o restante em minúsculo.

string = 'luiz Otavio'
# string[3] = 'ABC'
# TypeError: 'str' object does not support item assignment
# string é um tipo de dado imutavel, nao pode ser alterado

# string[:3] - fatiamento da string, ignora o indice 3
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string[3])
print(outra_variavel)

print(string)
print(string.capitalize())

numero = '1000'
print(numero.zfill(10))
