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

def excluir_cardapio(nome):#João Davi
    for item in cardapio:
        if item["Nome"] == nome:
            cardapio.remove(item)
            print(f"O item {nome} foi removido")
    return



cardapio = []



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
        nome = input("Digite o item que deseja excluir: ")
        excluir_cardapio(nome)
    elif escolha == 7:
        break


    
print("*****Programa Encerrado*****")




    




