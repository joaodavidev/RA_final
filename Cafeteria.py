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



def buscar_cardapio():#Ravaneda
    for indice, cardapio_item in enumerate(cardapio, start=1):
        item = cardapio_item["Nome"]
        preco = cardapio_item["Preco"]
        print(f"{indice}: {item} no valor de ${preco}")
    return

def excluir_cardapio( categoria, nome):#João Davi
    if categoria in cardapio:#verificar se a categoria existe
        valores = cardapio.get(categoria)#declarar os itens da categoria dentro do valores
        for items in valores:#analisar os itens da categoria
            if items['nome'] == nome:#verificar o "nome" dentro do item, que é um dicionario
                cardapio[categoria].remove(items)#remover o item inteiro
        print(f"O item {nome} foi removido de {categoria}")#print do feedback
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
    print("6. Ponto Extra")
    print("7. Encerrar Programa")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        categoria = input("Deseja adicionar qual categoria? ").lower()
        nome = input("Digite o item que deseja adicionar: ")
        preco = input("Digite o preço do item: ")
        adicionar_cardapio(cardapio, categoria, nome, preco)
    elif escolha == 2:
        buscar_cardapio()
    elif escolha == 4:
        categoria = input("Digite a categoria do item que deseja excluir: ")
        nome = input("Digite o item que deseja excluir: ")
        excluir_cardapio( categoria, nome)
    elif escolha == 7:
        break


    
print("*****Programa Encerrado*****")




    




