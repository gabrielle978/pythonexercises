#----DESAFIO_044----#
# elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
    # a vista dinheiro/cheque: 10% de desconto
    # a vista no cartão: 5% de desconto
    # em até 2x no cartão: preço normal
    # 3x ou mais no cartão: 20% de juros
"""
print('{:#^40}'.format(' LOJAS BASSIQUETE '))
valor = float(input('Digite o valor do produto: '))

condicao = int(input('Informe a condição de pagamento: '
                     '\n1 - À VISTA (Dinheiro ou cheque) '
                     '\n2 - À VISTA (Cartão) '
                     '\n3 - Parcelado em até 2x no cartão '
                     '\n4 - Parcelado em 3x ou mais no cartão\n'))

opc1 = valor - 10/100*valor
opc2 = valor - 5/100*valor
opc3 = valor
opc4 = valor + 20/100*valor

if condicao == 1:
    print('Opção 1 selecionada.'
          '\nSeu produto terá desconto de 10%'
          '\nDe R${:.2f} passará a custar R${:.2f}'.format(valor, opc1))
elif condicao == 2:
    print('Opção 2 selecionada.'
          '\nSeu produto terá desconto de 5%'
          '\nDe R${:.2f} passará a custar R${:.2f}'.format(valor, opc2))
elif condicao == 3:
    print('Opção 3 selecionada.'
          '\nDescontos não serão aplicados em seu produto nesta opção.'
          '\nValor a ser pago:', opc3)
elif condicao == 4:
    print('Opção 4 selecionada.')
    parcelas = int(input('Quantas parcelas? '))
    print('\nSeu produto terá acréscimo de 20% de juros'
          '\nDe R${:.2f} passará a custar {}'.format(valor, opc4))
    print('O total será de {} parcelas de R${:.2f} COM JUROS APLICADO'.format(parcelas, opc4/parcelas))
else:
    print('\033[1:31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!\033[m')
"""
#----DESAFIO_045----#
# crie um programa que faça o computador jogar jokenpô com você

import random
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura'] #itens 0,1 e 2
computador = random.randint(0, 2) #o computador sorteia um item para jogar

jogador = int(input('''Vamos jogar JOKENPÔ!'
                '\nFaça sua escolha...
    \033[1:36m[0] Pedra\033[m
    \033[1:35m[1] Papel\033[m
    \033[1:34m[2] Tesoura\033[m\n''')) #o jogador escolhe um item

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(0.5)


print('-='*11)
print('Jogador jogou: {}'.format(itens[jogador])) #o jogo informa qual posição o jogador escolheu dentro dos itens
print('Computador jogou: {}'.format(itens[computador])) #o jogo informa qual posição o computador escolheu dentro dos itens
print('-='*11)


if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('\033[7mEMPATE\033[m')

    elif jogador == 1:
        print('\033[7:32mJOGADOR VENCEU!\033[m')

    elif jogador == 2:
        print('\033[7:33mCOMPUTADOR VENCEU!\033[m')

    else:
        print('\033[7:31mJOGADA INVÁLIDA\033[m')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('\033[7:33mCOMPUTADOR VENCEU!\033[m')

    elif jogador == 1:
        print('\033[7mEMPATE\033[m')

    elif jogador == 2:
        print('\033[7:32mJOGADOR VENCEU!\033[m')

    else:
        print('\033[7:31mJOGADA INVÁLIDA\033[m')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('\033[7:32mJOGADOR VENCEU!\033[m')

    elif jogador == 1:
        print('\033[7:33mCOMPUTADOR VENCEU!\033[m')

    elif jogador == 2:
        print('\033[7mEMPATE\033[m')

    else:
        print('\033[7:31mJOGADA INVÁLIDA\033[m')

else:
    print('\033[1:31mCOMANDO INVÁLIDO, TENTE NOVAMENTE\033[')

