#----DESAFIO_042----#
#refazer o desafio 035, acrescentando o recurso de mistrar que tipo de triângulo será formado:
    #equilátero: todos os lados iguais
    #isósceles: dois lados iguais
    #escaleno: todos os lados diferentes

"""print('\033[7;30;44m-='*20, 'Analisador de triângulos', '=-'*20,'\033[m')

a = float(input('Digite o valor do primeiro seguimento em CM: '))
b = float(input('Digite o valor do segundo seguimento em CM: '))
c = float(input('Digite o valor do terceiro seguimento em CM: '))

if a < (b+c) and b < (c+a) and c < (a+b):
    print('É possível formar um triângulo')
    if a == b and b == c and c == a:
        print('Todos os lados são iguais.\nPortanto, trata-se de um \033[1:36mTRIÂNGULO EQUILÁTERO\033[m')
    elif a != c and a != b and c != b:
        print('Todos os lados são diferentes.\nPortanto, trata-se de um \033[1:32mTRIÂNGULO ESCALENO\033[m')
    elif:
        print('Dois lados são iguais.\nPortanto, trata-se de um \033[1:35mTRIÂNGULO ISÓSCELES\033[m')
else:
    print('Não é possível formar um triângulo')


"""

#----DESAFIO_043----#
# desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela:
    #abaixo de 18,5: abaixo do peso
    #entre 18.5 e 25: peso ideal
    #entre 25 até 30: sobrepeso
    #de 30 até 40: obesidade
    #acima de 40: obesidade mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso/(altura**2)

print('Seu IMC é de: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está \033[1:34mabaixo do peso\033[m')
elif imc > 18.5 and imc <= 25.0:
    print('Você está no \033[1:32mpeso ideal\033[m')
elif imc > 25.0 and imc <= 30.0:
    print('Você está \033[1:33macima do peso\033[m')
elif imc > 30.0 and imc <= 40.0:
    print('Você está na categoria \033[1:31mobesidade\033[m')
elif imc > 40.0:
    print('Você está na categoria \033[1:37mobesidade mórbida\033[m')
