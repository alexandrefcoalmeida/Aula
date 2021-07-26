#COMO CRIAR FUNÇÕES

#REALCE EM CABEÇALHO POR EXEMPLO
print('|','_' * 10,'|')
print('|','_' * 10, '|')
print('     MENU')
print('|','_' * 10, '|')
print('|','_' * 10,'|')

#AGORA USANDO UMA FUNÇÃO

#def=definition/realce=nome da função/()=parênteses :
def realce ():
    #corpo da função
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')

#COMO INVOCAR FUNÇÃO:

#programaprincipal
realce()
print('     MENU')
realce()

#Parametros em funções
#Enviar um dado para uma função é chamado de passagem de parâmetro
#s1 é a variável que será criada dentro da função e receberá o dado como parâmetro.

def realce (s1):
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')
    print(s1)
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')

realce('   Alexandre')

#AGORA USANDO CALCULO NA FUNÇÃO:

def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 7)

#PARÂMETROS OPCIONAIS:

def soma3 (x, y , z):
    res = x + y + z
    print(res)

# OU POSSO OMITIR PARAMETROS CASO EU DEFINA VALORES PADRÕES NO CABEÇALHO DA FUNÇÃO

def soma4 (x = 0, y = 0 , z = 0):
    res = x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2) # z foi omitido
soma3(1)   #y e z foram omitidos
soma3()    #x, y e z foram omitidos

#Exercício 1

#-Escreva uma rotina que crie uma borda ao redor de uma palavra para destacá-la
# como sendo um título. A rotina deve receber como parâmetro a palavra a ser destacada.
# O tamanho da caixa de texte deverá sr adaptável de acordo com om tamanho da palavra:

def borda(s1):
    tam = len(s1)
    #só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam, '+')
        print('|', s1, '|')
        print('+','-' * tam,'+')

borda('Olá mundo')
borda('Lógica de programação e algoritmos')

#ESCOPO DE VARIÁVEIS  ###################

def comida():
    print(ovos) #ESCOPO LOCAL

ovos = 12 #ESCOPO GLOBAL
comida()

#AGORA USANDO DUAS FUNÇOES ##########################

def comida():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6   #cada escopo local tem sua varíavel e não interferem entre si

comida()

####### OUTROS EXEMPLOS ###############################################

def comida():
    ovos = 'variável local de comida'
    print(ovos)

def bacon():
    ovos = 'variável local de bacon'
    print(ovos)
    comida()
    print(ovos)

ovos = 'variável global'
bacon()
print(ovos)

# ALTERAR UMA VARIAVEL GLOBAL SEM CRIAR UMA NOVA VARIAVEL NO ESCOPO LOCAL
# UTILIZANDO A INTRUÇÃO GLOBAL ANTES:

def comida():
 global ovos
 ovos = 'comida'

ovos = 'global'
comida()
print(ovos) # = comida

# FUNCTION VS PROCEDURE

#PROCEDIMENTO - Uma rotina sem retorno
#FUNÇÃO - Uma rotina que retorna um dado a quem a invocou.

#RETORNO DE VALORES EM FUNÇÕES

def soma3(x = 0, y = 0, z = 0):
 res = x + y + z
 return res

retornado = soma3(1,2,3)
print(retornado)

#forma alternativa simplificada
print(soma3(2,2))

#OU TAMBÉM :

retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2,)
retornado3 = soma3()
print('Somatórios: {}, {} e {}.'.format(retornado1, retornado2, retornado3))


# EXERCICIO: ###############################################
#Escreva uma função para validar uma string. Essa função recebe como parâmetro
# a string, o número mínimo e o máximo de caracteres. Retorne verdadeiro se o
# tamanho da string estiver entre os valores de mínimo e máximo, e falso, caso contrário
# não retorna nada e pede para digitar novamente:

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
      s1 = input(pergunta)
      tam = len(s1)
    return s1

x = valida_string('Digite uma string: ', 10, 30)  # tamanho da string
print('Você digitou a string {}. \n Dado válido. Encerrando o programa...'.format(x))


#########################################################################################

#TRATAMENTO DE ERROS (EXCEPTIONS):
#ZeroDivisionError - erro de divisão por zero
#ValueError - Erro de um dado nao esperado sendo digitado
#IndexError - erro de indice inexistente sendo acessado
#Lista completas de exceção: https://docs.python.org/pt-br/3/library/exceptions.html

#TRATANDO UMA EXCEÇÃO VALUE ERROR:
while True:
    try:
        x = int(input('Por favor digite um número: '))
        break
    except ValueError:
        print('Oops! Número inválido. Tente novamente...')

#TRATANDO UMA EXCEÇÃO DE ERRO DE DIVISÃO POR 0:

def div():
  try:
    num1 = int(input("Digite um número"))
    num2 = int(input("Digite um número"))
    res = num1 / num2
  except ZeroDivisionError:
    print("Ooops! Erro de divisão por zero...")
  except:
    print("Algo de errado aconteceu...")
  else:
    return res
  finally:
    print("Executará sempre!")

print(div())


# FUNÇÃO COMO PARÂMETRO DENTRO DE UMA FUNÇÃO (FUNÇÃO DENTRO DE FUNÇÃO):

def imprime_com_condicao(num, fcond):
  if fcond(num):
    print(num)

def par (x):
  return x % 2 == 0

def impar(x):
  return not par(x)

imprime_com_condicao(5, impar)

######################################################################################
#FUNÇÃO LAMBDA - Escrevido em uma só linha

res = lambda x: x * x
print(res)

soma = lambda x, y : x + y
print(soma(3, 5))



#COMO CRIAR UMA DOCSTRING (HELP DE UMA STRING)

def soma (x=0, y=0, z=0):
    """
    Função que soma até 3 valores inteiros
    :param x: valor inteiro opcional
    :param y: valor inteiro opcional
    :param z: valor inteiro opcional
    :return: soma inteira
    """
    return x + y + z
print(soma(3,2))
help(soma)

print('--------------------------------------------------')

#Exercício 2
#Escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne
#seu resultado. Faça uma validação dos dados por meio de outra função, permitindo que somente valores
#positivos sejam aceitos. Crie o help da sua função.

def valida_int(pergunta, min, max): #valida_int = valida dados inteiros
 x = int(input(pergunta))
 while ((x < min) or (x > max)):
     x = int(input(pergunta))
 return x
def fatorial(num):
    """
    Calcula a fatorial
    :param num: valor inteiro opcional
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1,num+1,1):
        fat *= i
    return fat

x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print('{}! = {}'.format(x,fatorial(x)))

print('--------------------------------------------------------------------------------')

#Suponha que você é um colecionador de jogos de videogame, escreva um algoritmo que permita cadastrar esses
#jogos iformando o nome e a qual videogame ele pertence. Para isso, crie um menu de opções
#contendo cadastrar novo item, listar tudo oque foi cadastrado e sair. Para realizar este
#exercício crie pelo menos uma função para cada item do menu. Além disso, armazene todos os dados
#em uma arquivo de texto que deve ser salvo em disco e manter os dados cadastrados.

def valida_int(pergunta, min, max): #valida_int = valida dados inteiros
 x = int(input(pergunta))
 while ((x < min) or (x > max)):
     x = int(input(pergunta))
 return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt') #rt = leitura e txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

#Programa principal

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)
while True:
 print('MENU')
 print('1 - Cadastrar novo item')
 print('3 - Listar Cadastros')
 print('4 - Sair')

 op = valida_int('Escolha a opção desejada', 1, 3)
 if op == 1:
     print('Opção de cadastrar novo item selecionada...\n')
     nomeJogo =input('Nome do jogo:')
     nomeVideogame = input('Nome do videogame:')
     cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
 elif op == 2:
     print('Opção de listar cadastro selecionada...\n')
     listarArquivo(arquivo)
 elif op == 3:
     print('Encerrando o programa...')
     break



#MANIPULAÇÃO DE ARQUIVOS

# Abrir arquivo: open()
# r Leitura
# w Escrita, apaga o conteúdo se já existir
# a Escrita, mas preserva o conteúdo se já existir
# b Modo binário
# t Modo TXT
# + Atualização (leitura e escrita)
#
# Fechar arquivo :     arquivo.close()
# Ler arquivo:         arquivo.read()
#                      arquivo.readlines()
# Escrever no arquivo: arquivo.write()
#






