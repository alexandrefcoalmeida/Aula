#ESTRUTURAS DE REPETIÇÃO

x = 1
print(x)
x = 2
print(x)
x = 3
print(x)
x = 4
print(x)
x = 5
print(x)

print('-------------------')

#SIMPLIFICADO: (em looping)

x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

print('--------------------')

# ESTRUTURA DE REPETIÇÃO (while): Irá repetir o bloco de instruções enquanto determinada
# condição se mantiver verdadeira. Caso contrário ocorre o desvio para a primeira
# linha de código após esse bloco de repetição.

#USANDO WHILE
x = 1
while (x <= 5):
    print(x)
    x = x + 1
print('----------------')
#VOLTANDO

x = 0
while (x <= 99):
    print(x)
    x = (x + 1)

print('---------------------------')

x = 0
while (x <= 100):
    print(x)
    x = (x + 1)

# VÁRIAVEIS CONTADORAS : Acrescentam valores constantes em uma variável.
# 1-Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado
# pelo usuário e que sejam números pares:
inicial = int(input('Qual valor deseja iniciar a contagem?'))
final = int(input('Qual valor deseja encerrar a contagem?'))
x = inicial
while(x <= final):
    if (x % 2 == 0): #verifica do inicio ao fim se o número é par de 2 em 2
        print(x)
    x = x + 1
print('-------------------------------------------------')
# VÁRIAVEIS ACUMULADORAS: Acumulam totais, como um somatório.
# 2 - Escreva um algoritmo que calcule a sua media de notas em determinada
# disciplina. Vamos assumir que a média final é dada pela média aritmética de
# cinco notas digitadas:

soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota:'.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print('Média final: {}'.format(media))

print('-----------------------------------------------------------')

#NOMENCLATURA DIFERENTE
soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota:'.format(cont)))
    soma += x # Equivalente a : soma = soma + x
    cont += 1 # Equivalente a : cont = cont + 1
media = soma / 5
print('Média final: {}'.format(media))

#VALIDANDO DADOS DE ENTRADA COM LAÇO DE REPETIÇÃO:

#Escreva um algoritmo que receba um valor do tipo inteiro via teclado no entanto, o
# programa só deve aceitar, obrigatoriamente, valores inteiros e positivos
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa,
# e um novo valor deve ser solicitado.

x = int(input('Digite um valor maior que 0'))
while (x <= 0):
    x = int(input('Digite um valor maior que 0'))
    print('Você digitou {}.Encerrando o programa...'.format(x))


print('------------------------------------------------------')

#INTERROMPENDO UM LOOP COM O BREAK
print('Digite uma mensagem que irei repetir para você')
print('Para sair escreva sair')
while True: #enquanto verdade / looping infinito
    texto = input('')
    print(texto)
    if texto == 'Sair':
        break
    print('Encerrando o programa...')
    break

print('------------------------------------------------')

#Voltando ao início do laço de repetição com continue:

while True:
    nome = input('Qual seu nome?')
    if (nome != 'Alexandre'):
      continue
    senha = input('Qual a sua senha')
    if (senha == 'alexandre'):
      break
print('Acesso concedido.')


print('------------------------------------')

#VALORES TRUTHY E FALSEY

#Dados Booleanos podem ser tratados como True ou False, em uma condição, seja esta de uma estrutura
# condicionada ou de um laço.

#FALSEY/FALSE: Número 0 (int ou float) ou string vazia.

#TRUTHY/TRUE: Qualquer outro dado.

nome = '' #string vazia
while not nome: #negando string vazia
    nome = input('Digite seu nome:')
valor = int(input('Digite um número qualquer:'))
if valor:
   print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')

    # como se fosse while True

print('---------------------------------------------------------------------')

# ESTRUTURA DE REPETIÇAO COM FOR (PARA):

for i in range(6):
    print(i)

print('----------------------------------------------------------------------')

for i in range(1,6,1): #para i no intervalo de um até seis, de um em um.
    print(i)


print('----------------------------------------------------------------------')

for i in range(10,0,-2):
    print(i)

print('----------------------------------------------------------------------')

#COM WHILE
x = 1
while (x < 6):
    print(x)
    x = x + 1

print('----------------------------------------------------------------------')

#Exercicios:

#1- Escreva um algoritmo que calcule a média dos numeros pares de 1 até 100 (1 e 100 inclusos).
# Implemente o laço usando for:

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}.'.format(media))

print('----------------------------------------------------------------------')
#Escreva um algoritmo em phyton que calcule a tabuada de todos os números de 1 até 10, e,
# para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10.

#UTILIZANDO 2 WHILES (Quando não sabemos quantas vezes vai se repetir)
tabuada = 1
while tabuada <= 10:
    print ('Tabuada do {}:'.format(tabuada))
    i = 1
    while i <= 10:
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

print('----------------------------------------------------------------------')
#UTILIZANDO FOR (Quando sabemos que as repetições serão finitas)

for tabuada in range (1, 11, 1):
    print('Tabuada do {}:'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))

#WHILE E FOR PODEM SE MISTURAR.

print('----------------------------------------------------------------------')

#FIM DA QUARTA AULA ----------------------------------------------------------








