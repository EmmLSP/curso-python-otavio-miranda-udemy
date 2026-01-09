"""
Exercicio 24
Faca um programa que peca o tamanho de um arquivo para
download (em MB) e a velocidade de um link de internet
(em Mbps), calcule e informe o tempo aproximado de download
do arquivo usando este link (em minutos).
"""

tam_arquivo_str = input('Digite o tamanho do arquivo para download (em MB): ')
tam_arquivo = int(tam_arquivo_str)
veloc_link_str = input('Digite a velocidade de internet (em Mbps): ')
veloc_link = int(veloc_link_str)

# 1 MB == 8 Mb

download = (tam_arquivo * 8) / (veloc_link * 60)
horas = int(download // 60)
minutos = int(download % 60)
segundos = int((download - int(download // 1)) * 60)
print(f'O download sera finalizado em {horas} horas, {minutos} minutos e {segundos} segundos')
