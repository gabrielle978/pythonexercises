#----DESAFIO_040----#
# criar um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final de acordo com a média atingida
    #media abaixo de 5.0: reprovado
    #media entre 5.0 e 6.9: recuperação
    #media 7.0 ou acima: aprovado

"""nota1 = float(input('Informe o valor da primeira nota: '))
nota2 = float(input('Informe o valor da segunda nota: '))

media = (nota1+nota2)/2

if media < 5.0:
    print('Sua média está abaixo de 5.0.\nResultado:\033[1:31mREPROVADO\033[m')
elif media <= 5.0 or media <= 6.9:
    print('Sua média está abaixo de 7.0.\nResultado:\033[1:33mRECUPERAÇÃO\033[m')
elif media >= 7.0:
    print('Sua média está acima de 7.0, parabéns!\nResultado:\033[1:32mAPROVADO\033[m')
"""

#----DESAFIO_041----#
#criar um programa que leia o ano de nascimento de um atleta e mostre a categoria de acordo com a idade
    #até 9 anos: mirim
    #até 14 anos: infantil
    #até 19 anos: junior
    #até 20 anos: sênior
    #acima: master
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Informe o seu \033[1mano de nascimento\033[m: '))

idade = ano_atual - ano_nasc

if idade <= 9:
    print('Categoria mirim')
elif idade >= 10 and idade <=14:
    print('Categoria infantil')
elif idade >= 15 and idade <= 19:
    print('Categoria júnior')
elif idade > 19 and idade < 21:
    print('Categoria sênior')
else:
    print('Categoria master')