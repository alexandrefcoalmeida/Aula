#ESTRUTURA DE DADOS
# Tuplas : () Estrutura de dados estática, a tupla é imutável, representada por parênteses
# Listas : [] Estrutura de dados dinâmica, podemos alterar de acordo com sua necessidade, adicionar ou remover dados.
# Dicionários : {} Estrutura de dados dinâmica, podemos alterar dados e tamanho, indexado por chaves.


# Tuplas () ###########-----------------------------------------------------------------------

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate' )
print(mochila)

print(mochila[0]) #print do elemento 1 - Indice 0
print(mochila[2]) #print do elemento 3 - Indice 2
print(mochila[0:2]) #print do elementos 1 e 2 ' - Indice 0 e 1
print(mochila[2:]) #print dos elementos a partir do índice 2
print(mochila[-1]) #print do último


#############################################

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

##############################################################


tam = len(mochila)
for i in range (0, tam, 1):
 print('Na minha mochila tem: {}'.format(mochila[i]))


#############################################################

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)
print(mochila)
print(upgrade)
print(mochila_grande) #('Machado', 'Camisa', 'Bacon', 'Abacate', 'Queijo', 'Canivete')

###############################################################
#DESEMPACOTAMENTO DE PARÂMETROS:

# Suponha que você quer realizar o somatório de diversos valores, porém não sabe quantos valores
# serão somados. pode ser que sejam somente 2, ou então 10 ou mesmo 100 números.
# Crie uma função capaz de receber um número variável de parâmetros:

def soma (*num):
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))


# Listas : [] ###----------------------------------------------------------------------------------------------#####

mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
print('Lista:', mochila)

####################################################################################
#MANIPULANDO LISTA

mochila[2] = 'Laranja'
print('Lista:', mochila)

############################

mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
print('Lista:', mochila)
                                                        #LISTAR
############################
mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
mochila.append('Ovos')                              #APPEND
print('Lista: ', mochila)


#############################
mochila.insert(1, 'Canivete')
print('Lista: ')                                  #INSERT

###############################
mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
del mochila[1]
print('Lista: ', mochila)


#OU
mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
mochila.remove('Ovos')
print('Lista: ', mochila)

#########################################
#STRINGS E LISTAS DENTRO DE LISTAS

mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
print(mochila[0]) #machado
print(mochila[2][1]) #a

###########################################
#STRINGS E LISTAS DENTRO DE LISTAS
mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
for item in mochila:
    for letra in item:
     print(letra, end='')
print() #MachadoCamisaBaconAbacate

###################################################
mochila = ['Machado', 'Camisa','Bacon', 'Abacate']
for i in range(0, len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j], end='')
    print()
#Machado
#Camisa
#Bacon
#Abacate

###################################################################

#EXERCICIO
# Imagine uma situação onde você deve realizar o cadastro de uma lista de compras
#em um sistema. Cada produto comprado deverá ser registrado com seu nome, quantidade
# e valor unitário:

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item'))
    item.append(input('Digite a quantidade'))
    item.append(input('Digite o Valor'))
    mercado.append(item[:])
    item.clear() #serve para limpar e reiniciar o processo de inserção
    print(mercado)

#####################################################
#outra maneira

mercado = []

for i in range(3):
    nome = input('Digite o nome o item:')
    qtd = int(input('Digite a quantidade:'))
    valor = float(input('Digite o valor:'))
    mercado.append([nome, qtd, valor])
print(mercado)


#########################################
#IMPRIMINDO A LISTA NA TELA

mercado = []

for i in range(3):
    nome = input('Digite o nome o item:')
    qtd = int(input('Digite a quantidade:'))
    valor = float(input('Digite o valor:'))
    mercado.append([nome, qtd, valor])



soma = 0
print('Lista de compras:')
print('-' * 20)
print('Item | Quantidade | Valor unitário | Total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma))


# Dicionários : {} -------------------------------------------------------------------------------------------------

# Métodos para dicionários
# values : obtém valores sobre dados  print(game.values())
# keys : obtém somente as chaves print(game.keys))
# items: obtém o par chave:dado


game = {'Nome': 'Super Mario',
        'Desenvolvedora': 'Nintendo',
        'Ano': 1990}
print(game)
print(game['Nome'])
print(game['Desenvolvedora'])
print(game['Ano'])

# values :
game = {'Nome': 'Super Mario',
        'Desenvolvedora': 'Nintendo',
        'Ano': 1990}
print(game.values())

###########

game = {'Nome': 'Super Mario',
        'Desenvolvedora': 'Nintendo',
        'Ano': 1990}
for i in game.values():
    print(i)


####### KEYS

game = {'Nome': 'Super Mario',
        'Desenvolvedora': 'Nintendo',
        'Ano': 1990}
print(game.keys))
 #OU

for i in game.values():
    print(i)

############# ITEMS
game = {'Nome': 'Super Mario',
        'Desenvolvedora': 'Nintendo',
        'Ano': 1990}
print(game.items())
## ou

for i in game.values():
    print('{} - {}'.format(i, j))

############################################################################################
#LISTA COM DICIONARIOS
games = []
game1 = {'Nome': 'Super Mario',
    'Desenvolvedora': 'Super Nintendo',
    'Ano': 1990}
game2 = {'Nome': 'Zelda',
    'Desenvolvedora': 'Nintendo 64',
    'Ano': 1998}
game3 = {'Nome': 'Pokemon',
    'Desenvolvedora': 'Game Boy',
    'Ano': 1999}
games = [game1, game2, game3]
print(games)

#INSERINDO CADASTRO VIA TECLADO --------------------------------------------------------

game = {}
games = []
for i in range(3):
        game['nome'] = input('Qual o nome do jogo?')
        game['videogame'] = input('Para qual vídeo-game foi lançado?')
        game['ano'] = input('Qual o ano de lançamento?')
        games.append(game.copy())
print('-' * 20)
for e in games:
        for i, j in e.items():
                print('O campo {} tem valor {}.'.format(i, j))

######################################################################
# DICIONARIO COM LISTAS DENTRO

games = {'nome':['Super Mario', 'Zelda', 'Pokemon'],
          'videogames':['Super Nintendo', 'Nintendo 64', 'Game Boy'],
          'ano':[1990,1998,1999]}
print(games)

###################################################
#AGORA INSERINDO VIA TECLADO


games = {'nome':[], 'videogame':[],'ano':[]}
for i in range(3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video-game foi lançado?')
    ano = input('Qual o ano de lançamento?')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)

#########################################
s1 = list('Algoritmos')
print(s1) #print separado  ['A', 'l', 'g', 'o', 'r', 'i', 't', 'm', 'o', 's']
print(''.join(s1)) #print agrupado  #Algoritmos

# startswith - verifica se caracteres existem no início da string
# endswith - verifica se caracteres existem no final da string
# lower - Converte string para minúscula
# upper - Converte string para maiuscula
# find - Busca a primeira ocorrencia de um padrão de caracteres em uma string
# rfind - Idêntido ao find, porém inicia uma busca da direita pra esquerda
# center - Centraliza uma string
# ljust, rjust - Ajustam uma string para esquerda e direta
# split - Divide uma string
# replace - Substitui caracteres em uma string
# lstrip, rstrip - Removem espaços em brancos à esquerda ou direita
# strip - Remove espaços em branco das extremidades.



#########################################################

s1 =  'Lógica de Programação e Algoritmos'
s1.startswith('Lógica')


s1 =  'Lógica de Programação e Algoritmos'
s1.lower().endswith('algoritmos')

s1 =  'Lógica de Programação e Algoritmos'
print(s1.upper())
print(s1.lower())

########################################################################################################################################








