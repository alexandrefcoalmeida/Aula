#Escreva um programa que leia o nome de um aluno e sua nota final. Em seguida, informe o conceito conforme a tabela abaixo.
# A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir:
# Todos os dados devem ser lidos do teclado, sendo que o nome do aluno é uma string e a nota final é um número real.
# Não é necessário armazenar os dados em uma estrutura de dados, basta imprimir na tela.
# Coloque todo o seu programa dentro de um laço de repetição e faça-o se encerrar quando uma determinada condição for satisfeita.
# A condição fica a seu critério, como por exemplo, encerrar o programa ao digitar a palavra sair, ou então uma nota inválida.
# Imprima na tela um teste do seu programa utilizando o seu nome e os dois últimos dígitos do seu RU para a nota:

dados = int(input('Inserir dados? 0-Não 1-Sim'))
if (dados == 1): #Validei se o usuário deseja inserir dados
 nome = (input('Nome do Aluno')) #armazenei nome
 nota = float(input('Nota final')) #armazenei nota
 conceito = '' #Declarei a variável conceito como string vazia
 if (nota >= 0 and nota <= 2.9): #validei se a nota é maior ou igual a 0 ou menor ou igual a 2.9
  conceito = 'E' #Atribuído E para variável conceito
 elif (nota >= 3.0 and nota <= 4.9): #validei se a nota é maior ou igual a 3.0 ou menor ou igual a 4.9
  conceito = 'D' #Atribuído D para variável conceito
 elif (nota >= 5.0 and nota <= 6.9): #validei se a nota é maior ou igual a 5.0 ou menor ou igual a 6.9
  conceito = 'C' #Atribuído C para variável conceito
 elif (nota >= 7.0 and nota <= 8.9): #validei se a nota é maior ou igual a 7.0 ou menor ou igual a 8.9
  conceito = 'B' #Atribuído B para variável conceito
 elif (nota >= 9.0 and nota <= 10): #validei se a nota é maior ou igual a 9.0 ou menor ou igual a 10
  conceito = 'A' #Atribuído A para variável conceito
 print('O aluno {} tirou a nota {} e se enquadra no conceito {}.'.format(nome, nota, conceito)) #Resultado final para o usuário
elif (dados == 0): #Validei se o usuário não deseja inserir dados
 print('Finalizando programa...') #Mensagem de finalização caso retorno na variável dados for 0.

print('Alexandre16')

