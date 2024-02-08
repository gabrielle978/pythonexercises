#----DESAFIO_054----#
#crie um programa que leia o ano de nascimento de sete pessoas.
#no final, mostre quantas pessoas já atingiram a maioridade e quantas não (21 anos)

'''from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?  '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1
print('Ao todo tiveram {} pessoas \033[1:34mmaior de idade\033[m'.format(totmaior))
print('E também tiveram {} pessoas \033[1:31mmenor de idade\033[m'.format(totmenor))

'''
#----DESAFIO_055----#
#faça um programa que leia o peso de cinco pessoas. No final mostre o maior e menor peso lidos
'''
peso_maior = 0
peso_menor = 0
for pesos in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pesos)))
    if peso >= peso_maior:
       peso_maior = peso
    else:
        peso_menor = peso
print('O \033[1:34mmaior\033[m peso lido foi {}kg'.format(peso_maior))
print('O \033[1:33mmenor\033[m peso lido foi {}kg'.format(peso_menor))


'''

#----DESAFIO_056----#
#desenvolva um programa que leia: nome, idade e sexo, de 4 pessoas
#no final do programa, mostre:
    #a média de idade do grupo;
    #qual o homem mais velho;
    #quantas mulheres têm menos de 20 anos

nomeh = ''
sexo = ''
tot_idade = 0
menosque20 = 0
idadeh = 0

for people in range(1, 5):
    print('----- {}ª PESSOA -----'.format(people))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    tot_idade += idade
    if sexo == 'M':
        if idade >= idadeh:
            idadeh = idade
            nomeh = nome
    elif sexo == 'F':
        if idade < 20:
            menosque20 += 1
print('A média de idades foram de {} anos'.format(tot_idade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeh, nomeh))
print('O total de mulheres abaixo dos 20 anos foi de: {} mulheres'.format(menosque20))
