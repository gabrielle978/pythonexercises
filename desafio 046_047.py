"""i = int(input('INÍCIO: '))
#f = int(input('FIM: '))
#p = int(input('PASSO: '))

for c in range(i, 0, -1): # i = contador, 0 = até chegar em 0, -1 = intervalo, no caso i-1 até chegar em 0
    print(c)
print('FIM')
"""
#----DESAFIO_046----#
#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
#indo de 10 a zero, com uma pausa de 1s entre eles

"""
from time import sleep
import emoji

print('Vamos estourar fogos de artifício?\nSe prepare para a contagem...')

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)

print(emoji.emojize('BOOM!!!' 
':fireworks:', language='alias'))
"""

#----DESAFIO_047----#
#crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for i in range(2, 51, 2):
    print(i)
print('FIM')