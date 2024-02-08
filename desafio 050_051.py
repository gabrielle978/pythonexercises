#----DESAFIO_050----#
#desenvolva um programa que leia seis números inteiros e mostre apenas:
    #a soma dos que forem pares
    # se o valor digitadp for ímpar, desconsidere-o
"""
s = 0 #variável que armazena soma
cont = 0 #contador que guarda o número e passa para o próximo
for l in range(1, 7):
    entrada = int(input('Digite o {} valor: '.format(l)))
    if entrada % 2 == 0: #se a divisão do número por 2 for igual a 0
        s += entrada # a variavel s acumula o valor digitado
        cont += 1 #e o contador guarda o número e passa para o próximo
print('A Soma dos números pares informados é: {}'.format(s))

"""
#----DESAFIO_051----#
#desenvolva um programa que leia o primeiro termo e a razão de uma pa;
#no final mostre os 10 primeiros termos dessa pa


a1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Informe a razão desta P.A: '))

#an = a1+(n-1)*r
#a10 = a1+(10-1)*r
a10 = a1 + (10-1) * r
for i in range(a1, a10, r):
    print('{}'.format(i), end='\033[1:35m > \033[m')
