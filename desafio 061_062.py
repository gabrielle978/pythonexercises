#----DESAFIO_061----#
#refaça o desafio 051, usando a estrutura WHILE
'''print('Gerador de P.A')
print('-='*12)
a1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Informe a razão desta P.A: '))

an = a1
cont = 1
#an = a1+(n-1)*r

while cont <= 10:
    print('{}'.format(an), end='\033[1:35m > \033[m')
    an += r
    cont += 1
print('FIM')'''


#----DESAFIO_062----#
#melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#o programa encerra quando ele disser que quer mostrar 0 TERMOS.

print('Gerador de P.A')
print('-='*12)
a1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Informe a razão desta P.A: '))

an = a1
cont = 1
total = 0
mais = 10
#an = a1+(n-1)*r

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(an), end='\033[1:35m > \033[m')
        an += r
        cont += 1
    print('BREAK')
    mais = int(input('Quantos termos a mais deseja visualizar?: '))

print('Finalizando o programa...')