#Faça uma função que receba o nome e sobrenome de uma pessoa e retorne a primeira letra de seu nome e seu sobrenome
#concatenando com a string @algoritmos.com.br. No algoritmo principal deverá ser apresentada a mensagem ao usuário contendo seu nome completo e seu email.
#Imprima na tela um teste do seu programa utilizando o seu nome e sobrenome concatenado com os dois últimos dígitos do seu RU:

#Exemplo: Sra Luciane Kanashiro, seu email é lkanashiro16@algoritmos.com.br


nome = input('Digite seu nome') #armazenado nome
sobrenome = input('Digite seu sobrenome') #armazenado sobrenome
print(nome[0:1] + sobrenome + '16' + '@algoritmos.com.br') #fatiado primeira string do nome
# e concatenado sobrenome com 16 e mais o e-mail.


