"""
Exercicio 041
Desenvolva uma logica que leia o peso e a altura
e uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

formula: IMC = peso (Kg) / altura(m)²

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida
"""

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO ideal')
elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce esta com SOBREPESO')
elif 30 <= imc < 35:
    print('Voce esta em OBESIDADE grau I')
elif 35 <= imc < 40:
    print('Voce esta em OBESIDADE grau II')
else:
    print('Voce esta em obesidade mórbida, cuidado!')
