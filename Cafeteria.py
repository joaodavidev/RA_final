#Cafeteria
#Ravaneda -> Alterar itens do cardapio
#João Davi -> Excluir itens do cardapio
#Lyra -> Adicionar itens ao cardapio
#Gustavo -> Buscar itens no cardapio
#Guilherme -> Listar todos os itens do cardapio e ponto extra



def adicionar_cardapio(cardapio,nome,preco):
    cardapio_item = {"Nome": nome,
                "Preço": preco}
    cardapio.append(cardapio_item)
    print(f"O item {nome} foi adicionado no cardápio com preço R$ {preco}")
    return 

cardapio = []



while True:
    print("\nMenu da Cafeteria:")
    print("1. Adicionar itens ao1 Cardápio")
    print("2. Buscar itens no Cardápio")
    print("3. Alterar itens do Cardápio")
    print("4. Excluir itens do Cardápio")
    print("5. Listar todos os itens do Cardapio")
    print("6. Ponto Extra")
    print("7. Encerrar Programa")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        nome = input("Digite o item que deseja adicionar: ")
        preco = int(input("Digite o preço do item: "))
        adicionar_cardapio(cardapio, nome, preco)
    elif escolha == 7:
        break
print("*****Programa Encerrado*****")


    




