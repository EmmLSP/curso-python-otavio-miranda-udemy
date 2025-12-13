# Introdução aos blocos de código + if / elif / else (condicionais)

# if  / elif       / else
# se  / se nao se  / se nao

entrada = input('Voce quer "entrar" ou "sair"? ').lower().strip()

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Voce nao digitou nem entrar e nem sair')

print('Fora dos Blocos')
