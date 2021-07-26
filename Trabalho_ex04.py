tabela = [] #declaração de lista
pergunta = int(input('Deseja cadastrar um novo produto no estoque? 1 - Sim / 0 - Não ')) #opção de entrada
while pergunta == 1: #enquanto a opção digitada for 1 o programa executa
    produto = {} #declaração de dicionário
    produto['codigo'] = int(input('Insira o código do produto: ')) #variavel código recebendo o valor digitado

    if produto['codigo'] == 0: #se codigo digitado for igual a 0 finaliza o programa
        print('Encerrando programa...') #mensagem de retorno
        break

    produto['estoque'] = int(input('Insira a quantidade do produto: ')) #variavel estoque recebendo o valor digitado
    produto['minimo'] = int(input('Insira a quantidade mínima do produto em estoque: ')) #variavel minimo recebendo o valor digitado

    tabela.append(produto) #adiciona produto na lista 'tabela'
    pergunta = int(input('Deseja cadastrar um novo produto no estoque? 1 - Sim / 0 - Não ')) #valida se o usuário deseja cadastrar novo produto

if len(tabela) > 0: #se lista for maior que 0
    print('Tabela de estoque dos produtos:') #imprime tabela
    print("Código | Estoque |  Mínimo") #imprime colunas

    for produto in sorted(tabela, key=lambda item: item['codigo']):  #método de ordenação em ordem crescente pelo código do produto
        print(str(produto['codigo']) + '      |    ' + str(produto['estoque']) + '    |     ' + str(produto['minimo'])) #imprime produtos