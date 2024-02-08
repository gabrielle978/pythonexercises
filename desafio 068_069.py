#----DESAFIO_68----#
#faça um programa que jogue par ou impar com o computador.
#o jogo só ser-a interrompido quando o jogador perder. Mostrando o total de vitórias consecutivas que o jogador teve ao fim do jogo
'''from random import randint
from time import sleep

print('------'*5, '\nVAMOS JOGAR? ÍMPAR OU PAR?\n', '-----'*5,)
sleep(0.5)

cont = 0


while True:
    escolha_j = int(input('Me diga um número: '))
    escolha_pc = randint(0, 10)
    total = escolha_pc + escolha_j
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'O computador jogou \033[1:31m{escolha_pc}\033[m, e você jogou \033[1:33m{escolha_j}\033[m.'
          f'\nO total foi de \033[1:35m{total}\033[m')
    print(f'O resultado foi...\033[1:35mPAR\033[m' if total % 2 == 0 else 'O resultado foi...\033[1:35mÍMPAR\033[m')
    if tipo == 'I':
        if total % 2 != 0:
            print('\033[1:32mVocê ganhou\033[m!')
            cont += 1
        else:
            print('\033[1:31mVocê perdeu!\033[m')
            break
    elif tipo == 'P':
        if total % 2 == 0:
            print('\033[1:32mVocê ganhou!\033[m')
            cont += 1
        else:
            print('\033[1:31mVocê perdeu!\033[m')
            break
print(f'Você ganhou {cont} vez(es). \033[1mParabéns!\033[m')
sleep(1)
'''

#----DESAFIO_69----#
#crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continhuar
#ao fim, mostre:
    #quantas pessoas tem mais de 18 anos;
    #quantos homens foram cadastrados;
    #quantas mulheres tem menos de 20 anos
from time import sleep

print('='*30, '\nCADASTRO DE PESSOAS\n','='*30)
homem = maior = mMenosVinte = 0

while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F'and idade <= 20:
        mMenosVinte += 1
    mais_um = ' '
    while mais_um not in 'SN':
        print('-'*30)
        mais_um = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if mais_um == 'N':
        break
print('Finalizando o programa...')
sleep(0.5)
print(f'\033[4:32mPessoas maiores de 18 anos:\033[m {maior}'
      f'\n\033[4:34mHomens cadastrados:\033[m {homem}'
      f'\n\033[4:31mMulheres abaixo de 20 anos:\033[m {mMenosVinte}')
sleep(0.5)
print('Volte sempre!')
sleep(0.5)









