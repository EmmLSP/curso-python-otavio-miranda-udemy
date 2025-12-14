# Variáveis, constantes e complexidade de código

"""
CONSTANTE = "Variaveis" que nao vao mudar
Muitas condicoes no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# velocidade > limite and local dentro do range
# 61 > 60 and 099 >= 99 and 099 <= 101 = True and True and True = True
# 61 > 60 and 100 >= 99 and 100 <= 101 = True and True and True = True
# 61 > 60 and 101 >= 99 and 101 <= 101 = True and True and True = True

# 60 > 60 and 099 >= 99 and 099 <= 101 = False and True and True = False
# 61 > 60 and 98 >= 99 and 98 <= 101 = True and False and True = False
# 61 > 60 and 102 >= 99 and 102 <= 101 = True and True and False = False

velocidade = 61 # velocidade atual do carro
local_carro = 99 # local em que o carro esta na estrada

RADAR_1 = 60    # velocidade maxima do radar 1
LOCAL_1 = 100   # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
range_menos_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
range_mais_1 = local_carro <= (LOCAL_1 + RADAR_RANGE)
# carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = range_menos_1 and range_mais_1
carro_multado_radar_1 = vel_carro_passou_radar_1 and carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Velocidade do carro passou no radar 1')

if carro_passou_radar_1:
    print('Carro passou dentro do range do radar 1')

if carro_multado_radar_1:
    print('Carro passou do limite de velocidade e foi multado no radar 1')

if not vel_carro_passou_radar_1 and not carro_passou_radar_1:
    print('Carro nao passou da velocidade e nem foi multado dentro do range do radar 1')
