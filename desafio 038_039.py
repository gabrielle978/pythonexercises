#----DESAFIO_038----#
#escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:
# o primeiro valor é maior, o segundo valor é maior, ou não existe valor maior, os dois são iguais

"""n1 = int(input('\033[1:33mDigite um número:\033[m '))
n2 = int(input('\033[1:33mDigite outro número:\033[m '))

if n1>n2:
    print('O \033[1:34mprimeiro\033[m valor é maior')
elif n2>n1:
    print('O \033[1:36msegundo\033[m valor é maior')
else:
    print('Não existe valor maior. Os dois números são \033[1:35miguais\033[m.')
"""

#----DESAFIO_039----#
#faça um programa que leia o ano de nascimento de um jovem, e informe de acordo com a idade:
    #se ele ainda vai se alistar ao serviço militar;
    #se é a hora de se alistar;
    #se já passou do tempo do alistamento;
#o programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = atual - nasc


if idade < 18:
    print('Em breve você deverá se alistar para o exército'
          '\nSeu alistamento será no ano de {}'.format(atual + 18))
elif idade == 18:
    print('Caso não tenha se alistado, \033[1:32mvocê está na idade de se alistar ao exército!\033[m')
elif idade > 18:
    print('Você passou \033[1:31m{}\033[m ano(s) do prazo de alistamento ao exército'
          '\nSeu alistamento deveria ter sido no ano de {}'.format(18-idade, atual - (idade-18)))