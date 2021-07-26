import random #importado biblioteca random

pergunta = int(input('Deseja inserir uma doação? Digite 0 - Não | 1 - Sim')) #perguntado se usuário deseja prosseguir
listaSorteio = [] #declarada variável lista de doadores

while (pergunta == 1): #verificando se resposta é igual a um para prosseguir.
 nome = input(('Digite o seu nome')) #solicitado nome do doador
 doacao = int(input('Digite o valor da doação:')) #solicitado quantia de doação
 if (doacao >= 10): #valida se o valor mínimo de doação é 10.
  valor = int(doacao / 10) # calculado número de vezes que a pessoa irá aparecer na lista
  for i in range(valor): #laço de repetição com número de vezes que a pessoa concorrerá.
   listaSorteio.append(nome)  #adiciona nome do doador na lista
  pergunta = int(input('Deseja inserir uma doação? Digite 0 - Não | 1 - Sim')) #valida se usuário deseja inserir outro nome.
 else:
  print('A doação minima para ser sorteado é de R$10') #valida valor mínimo para que o usuário seja sorteado.

if (len(listaSorteio) != 0): #imprime a lista de sorteio no final se ela não estiver vazia.
 random.shuffle(listaSorteio) #embaralha nomes
 ganhador = random.choice(listaSorteio) #sorteia o ganhador
 print('O ganhador foi ' + ganhador) #imprime na tela o ganhador.



