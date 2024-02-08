#----DESAFIO_66----#
#crie um programa que leia vários números int. O programa só vai parar quando o usuário digitar 999 (condição de parada)
#no final mostre quantos números foram digitados e qual foi a soma entre eles, considerando a flag

'''print('-'*30, '\nLEITOR NÚMERICO\n', '-'*30)

cont = n = s = 0
n = int(input('Informe um número[999 PARA SAIR DO PROGRAMA]: '))

while True:
    n = int(input('Informe um número[999 PARA SAIR DO PROGRAMA]: '))
    if n == 999:
        print('Finalizando o programa')
        break
    s += n
    cont += 1

print(f'Foram digitados {cont} números e a obteve soma de {s}')
'''


#----DESAFIO_67----#
#faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#o programa será interrompido quando o número solicitado for negativo

print('\033[1:35m-_-_-'*5, '\nTABUADA VIRTUAL\n', '-_-_-'*5,'\033[m')

n = 1
cont = 1

while True:
    n = int(input('Qual valor desejaria ver a tabuada? '))
    print('-' * 30)
    if n < 1:
        print('Encerrando o programa...')
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n * cont}', end='\n')
        cont += 1
    print('-' * 30)
    cont = 1
