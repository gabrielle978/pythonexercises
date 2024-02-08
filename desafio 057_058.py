'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
'''

#----DESAFIO_057----#
#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#caso esteja errado, peça a digitação corretamente até ter o valor correto

'''entrada = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]

while entrada not in 'MF':
    print('Não foi possível identificar sua resposta.')
    entrada2 = str(input('Informe o sexo novamente [M/F]: ')).strip().upper()[0]
    entrada = entrada2

print('Você informou [{}]'.format(entrada))'''

#----DESAFIO_058----#
#melhore o jogo do desafio 028, onde o computador vai 'pensar' em um número até 0 a 10.
#Porém, agora o jogador vai tenar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import random

print('Sou seu computador! acabei de pensar em um número entre 0 e 10...\nSerá que você consegue adivinhar?')
acertou = False
num_random = random.randint(0,10)
tentativas = 0

while not acertou:
    num_user = int(input('Escreva seu palpite: '))
#    print('Resposta incorreta')
#    num_user_again = int(input('Pense em novamente um número entre 0 e 10 e escreva seu palpite: '))
#    num_user = num_user_again
    tentativas += 1
    if num_random == num_user:
        print('\033[1:32mParabéns! Você acertou com \033[7:32m{}\033[m \033[1:32mtentativas\033[m.\n'
              'O número sorteado era: \033[1:32m{}\033[m'.format(tentativas, num_random))
    else:
        if num_random > num_user:
            print('Mais...tente novamente')
        else:
            print('Menos...Tente novamente')