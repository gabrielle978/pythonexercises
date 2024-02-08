#----DESAFIO_063----#
#escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci
    #ex = 0>1>1>3>>5>8

'''print('-----'*6, '\nSequência de Fibonacci\n','-----'*6)

n = int(input('Quantos termos você quer mostrar? : '))
cont = 3
a1 = 0
a2 = 1
print('{} > {}'.format(a1, a2), end=' > ')
while cont <= n:
    a3 = a1 + a2
    print('{}'.format(a3), end=' > ')
    a1 = a2
    a2 = a3
    cont += 1

print('FIM')
'''

#----DESAFIO_064----#
#crie um programa que leia *varios* números inteiros pelo teclado
#o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#no final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag de parada)

'''contador = n = soma = 0
n = int(input('[Caso deseja encerrar o programa, digite 999]\nInforme um número: '))

while n != 999:
    soma += n
    contador += 1
    n = int(input('[Caso deseja encerrar o programa, digite 999]\nInforme um número: '))
   #if n == 999:
    #soma -= 999 
    #contador -= 1


print('Foram digitados {} números.\nA soma dos números digitados é de: {}'.format(contador, soma))
'''



#----DESAFIO_065----#
#crie um programa que leia VÁRIOS números inteiros pelo teclado, no final da execução mostre:
    #a média entre todos os valores
    #qual foi o MENOR e o MAIOR valor lido
#o programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores
from time import sleep

resp = 'S'
vezes = soma = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    vezes += 1
    if vezes == 1: #caso apenas para o primeiro n informado
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resp = str(input('Gostaria de continuar?[S/N]: ')).upper().strip()[0]
    sleep(0.5)

media = soma/vezes
print('A média da soma dos valores foi de: {:.2f}\nO maior número foi {} \nO menor número foi: {}'.format(media, maior, menor))
print('Finalizando o programa...')
