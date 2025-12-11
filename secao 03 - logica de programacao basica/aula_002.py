
# funcao print() - recebe
# argumentos e imprime os na tela

# \r\n -> CRLF (windows)
# \n -> LF (linux / mac)

print(12, 34, 1011, sep='-', end='##\n')
print(12, 34, 1011, sep='-', end='\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

# o Python diferencia letras minusculas de letras maisculas
# o Python é case sentive
