#Cafeteria
#Ravaneda -> Alterar itens do cardapio
#João Davi -> Excluir itens do cardapio
#Lyra -> Adicionar itens ao cardapio
#Gustavo -> Buscar itens no cardapio
#Guilherme -> Listar todos os itens do cardapio e ponto extra

def adicionar_cardapio(cardapio, categoria, nome, preco):#Lyra
    cardapio_item = {"nome": nome,
                     "preco": preco}
    if categoria in cardapio:
        cardapio[categoria].append(cardapio_item)
        print(f"\nO item {nome} foi adicionado no cardápio na categoria {categoria} com preço R$ {preco}")
    else:
        print("\nErro: Categorias existentes: Bebidas, Entradas, Pratos Princiais e Sobremesas")
    return

def buscar_cardapio(cardapio, categoria):#Ravaneda
    if categoria in cardapio:
        itens = cardapio[categoria]
        print(f"\n{categoria.upper()}")
        if itens:
            for indice,item in enumerate(itens, start=1):
                nome = item["nome"]
                preco = item["preco"]
                print(f"{indice}. {nome} no valor de R${preco}")
        else:
            print("Não possui nenhum item!")
    else:
        print("Erro: Categoria Inexistente!")
    return

def alterar_item_cardapio(cardapio, categoria, nome_veio, nome_novo, preco_novo):        #Gustavo
    if categoria in cardapio: #Verificar se a categoria existe
        for item in cardapio[categoria]: #Criar um laço de repetição(Para cada item que estiver dentro da categoria)
            if item['nome'] == nome_veio: #Verificando se o  nome antigo existe dentro da categoria
                item['nome'] = nome_novo #Está mudando  o nome antigo para o  nome novo.
                item['preco'] = preco_novo #Está mudando o preco antigo para o preco novo
                print(f"\n{nome_veio} foi atualizado para {nome_novo} com o novo preço de R$ {preco_novo}") #Mostra que as categorias foram atualizadas corretamente
                return
        print(f"\nErro: {nome_veio} não encontrado na categoria {categoria}") #Mostra que a categoria nao foi encontrada
    else:
        print("\nErro: Categorias existentes: Bebidas, Entradas, Pratos Princiais e Sobremesas") #Mostra todas as categorias existentes se tiver colocado uma errada.
    return

def excluir_cardapio( categoria, nome):#João Davi Dev
    if categoria in cardapio:#verificar se a categoria existe
        valores = cardapio.get(categoria)#declarar os itens da categoria dentro do valores
        for items in valores:#analisar os itens da categoria
            if items['nome'] == nome:#verificar o "nome" dentro do item, que é um dicionario
                cardapio[categoria].remove(items)#remover o item inteiro
        print(f"\nO item {nome} foi removido de {categoria}")#print do feedback
    return

def cardapio_completo(cardapio):    #Guilherme
    print("\nCardapio Completo: ")
    indice_ajustado = 1 # Variavel necessaria para iniciar a contagem dos indices.
    for categoria, itens in cardapio.items(): # variaveis necessarias para iterar sobre os itens de todas as categorias.
        for indice, item in enumerate(itens, start=indice_ajustado): # Looping usado para numerar os itens do cardapio.
            nome = item["nome"] # Atribui a variavel "nome" com o nome do item dentro do dicionario.
            preco = item["preco"] # Atribui a variavel "preco" com o preco do item dentro do dicionario.
            print(f"{indice}. {nome} no valor de R$ {preco}") # Modelo em que vai aparecer os itens do dicionario.
            indice_ajustado += 1 # Necessario para a contagem dos itens serem subsequentes.
    return

cardapio = {
            "bebidas": [],
            "entradas": [],
            "pratos principais": [],
            "sobremesas": []
            }

while True:
    print("\nMenu da Cafeteria:")
    print("1. Adicionar itens ao Cardápio")
    print("2. Buscar itens no Cardápio")
    print("3. Alterar itens do Cardápio")
    print("4. Excluir itens do Cardápio")
    print("5. Listar todos os itens do Cardapio")
    print("6. Encerrar Programa")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        categoria = input("Deseja adicionar qual categoria? ").lower()
        nome = input("Digite o item que deseja adicionar: ").capitalize()
        preco = input("Digite o preço do item: ")
        adicionar_cardapio(cardapio, categoria, nome, preco)
    elif escolha == 2:
        categoria = input("Digite a categoria que deseja visualizar: ")
        buscar_cardapio(cardapio, categoria)
    elif escolha == 3:
        categoria = input("Digite a categoria do item que deseja alterar: ").lower()
        nome_veio = input("Digite o nome do item que deseja alterar: ").capitalize()
        nome_novo = input("Digite o novo nome do item: ")
        preco_novo = input("Digite o novo preço do item: ")
        alterar_item_cardapio(cardapio, categoria, nome_veio, nome_novo, preco_novo)
    elif escolha == 4:
        categoria = input("Digite a categoria do item que deseja excluir: ")
        nome = input("Digite o item que deseja excluir: ")
        excluir_cardapio( categoria, nome)
    elif escolha == 5:
        cardapio_completo(cardapio)
    elif escolha == 7:
        break

print("*****Programa Encerrado*****")
