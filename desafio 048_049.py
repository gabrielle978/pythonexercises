# ----DESAFIO_048----#
# faça um programa que calcule a soma entre todos os números ímpares entre:
# 1 e 500
# que sejam multiplos de 3;

"""cont = 0
soma = 0
for c in range(1, 501, 2):
    #print(c)
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} valores solicitados é {}'.format(cont, soma))
"""


#----DESAFIO_049----#
#refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
#só que utilizando agora o laço FOR
i = 0
n = int(input('Digite o número que deseja consultar a tabuada: '))
print('A tabuada do número \033[1:33m{}\033[m é:\n'.format(n))

for c in range(n, n+10, +1):
    i = i+1
    print('\033[1:33m{} * {} = {} \033[m'.format(n, i, n*i), end='\n')
print('\033[1:33m----\033[m'*10)
