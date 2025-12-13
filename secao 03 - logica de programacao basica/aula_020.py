# Exercício de programação com if e comparação

# Python utiliza tabela unicode para fazer comparacao com letras
# primeiro_valor = 'a' e segundo_valor = 'b' - 'a' < 'b'
# segundo_valor='b' e maior do que primeiro_valor='a'
# primeiro_valor = 'b' e segundo_valor = 'a' - 'b' > 'a'
# primeiro_valor='b' e maior do que segundo_valor='a'

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} e maior ou igual do que {segundo_valor=}')
else:
    print(f'{segundo_valor=} e maior do que {primeiro_valor=}')
