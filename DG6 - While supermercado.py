import os

#cria primeiro as listas
listaprodutos = []
listapreços = []
acima50 = 0 #contador de produtos acima de 50 reais.

while True:

    os.system('cls')

    nomeproduto = str(input('Digite o nome do produto. Ou digite "sair" para finalizar.').strip)
    if nomeproduto.lower() == "sair":
        break

    preçoproduto = float(input('Digite o preço do produto.'))
    
    #função que adiciona mais dados na lista
    listaprodutos.append(nomeproduto)
    listapreços.append(preçoproduto)

    valmax = max(listapreços)
    acima50 = listapreços > 50

    print(listaprodutos, listapreços)