#----DESAFIO_059----#
#crie um programa que leia dois valores e mostre na tela um menu:
    #[1] somar
    #[2] multiplicar
    #[3] maior
    #[4] novos números
    #[5] sair do programa
#seu programa deverá realizar a operação solicitada em cada caso
'''from time import sleep

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

cont = 0
escolhido = 0

while escolhido != 5:
    print('Escolha a ação a ser realizada com os valores informados:\n[1] SOMAR\n[2] MULTIPLICAR\n[3] OBTER O MAIOR VALOR\n[4] OBTER NOVOS VALORES\n[5] SAIR DO PROGRAMA')
    escolhido = int(input('Qual a sua opção? '))
    if escolhido == 1:
        print('A soma dos valores informados é: {}'.format(n1+n2))
    elif escolhido == 2:
        print('A multiplicação dos valores informados é: {}'.format(n1*n2))
    elif escolhido == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número dentre os informados foi: {}'.format(maior))
    elif escolhido == 4:
        print('Informe os números novamente')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif escolhido == 5:
        print('Finalizando o programa...')
    else:
        print('Não foi possível identificar a ação.')
    print('=-='*10)
    sleep(2)

print('Volte sempre!')'''


#----DESAFIO_060----#
#faça um programa que leia um número qualquer e mostre seu fatorial.
    #ex: 5! = 5*4*3*2*1 = 120

# from math import factorial
#f = factorial(n)

n = int(input('Informe o valor que deseja ver seu fatorial: '))

f = n
fatorial = 1
while f > 0:
    print('{}'.format(f), end='')
    print(' x ' if f > 1 else ' = ', end='')
    fatorial *= f
    f -= 1
print('O fatorial de {}! é: {}.'.format(n, fatorial))