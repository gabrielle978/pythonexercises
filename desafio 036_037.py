#----DESAFIO_036----#
#programa para aprovar o empréstimo bancário para a compra de uma casa
#o programa recebe o valor da casa e o salario do comprador e em quantos anos ele pagará.
#calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado.

"""valor_casa = float(input('Qual o valor da casa que deseja comprar? '))
salario_comprador = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos deseja pagar o imóvel? '))

valor_prestacao = valor_casa/(anos*12)
limite_prestacao = salario_comprador*0.3

if valor_prestacao <= limite_prestacao:
    print('O seu empréstimo foi \033[1:32maprovado!\033[m\nDe acordo com o valor informado do imóvel de R${:.2f}'
          '\ne salário de R${:.2f}, você conseguirá pagar em {} anos.'
          'O valor de cada parcela será de R${:.2f}'.format(valor_casa, salario_comprador, anos, valor_prestacao))
elif valor_prestacao >= limite_prestacao:
    print('O seu empréstimo foi \033[1:31mnegado.\033[m\nO valor da parcela excede o correspondente aos 30% de seu salário.\n'
          'Valor parcela: R${:.2f}\nLimite prestação: R${:.2f}'.format(valor_prestacao, limite_prestacao))
else:
    print('Algo deu errado. Tente novamente.')"""



#----DESAFIO_037----#
#escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')