#----DESAFIO_052----#
#faça um programa que leia um número inteiro e diga se ele é ou não um número primo
"""
n = int(input('Informe o número que deseja descobrir se é um \033[1:33mnúmero primo: \033[m'))
total = 0
for i in range(1, n +1):
    if n % i == 0: #se o número informado dividido por um range entre 1 e ele mesmo tiver resto == 0
        print('\033[1:34m', end='')
        total +=1
    else:
        print('\033[1:33m', end='')
    print('{} '.format(i), end='') #o comando end informa para continuar na mesma linha
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))

if total == 2:
    print('Por isso, \033[1:34mo número {} é PRIMO!\033[m'.format(n))
else:
    print('Por isso, \033[1:33mo número {} NÃO É PRIMO!\033[m'.format(n))
"""

#----DESAFIO_053----#
#crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços

frase = str(input('Digite uma frase e descubra se ela é ou não um palíndromo: ')).strip().upper() #tira os espaços excedentes e põe em maiúsculo
junto = ''.join(frase.split()) #separa as palavras e junta as palavras separadas
inverso = junto[::-1]

'''for letra in range(len(junto)-1, -1, -1): #o contador começa a contagem do menos um, para não ignorar o último índice da frase
                                             #vai até a primeira letra (índice 0, ou seja, a contagem começa do -1)
                                             #e vai voltando a contagem de trás para frente
    inverso += junto[letra]
'''
print('O inverso de {}, é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo')