import os
os.system('cls' if os.name == 'nt' else 'clear')

preçobase = float(input('Informe o valor do produto.'))

lista1 = [1,2]

print(''' 
Selecione o número da forma de pagamento:
1 - Dinheiro
2 - Cartão''')


formaselecionada = int(input(''))

if formaselecionada == 1:
    dinheiro = preçobase * 0.90
    print(f'O valor será de {dinheiro} reais.')

elif formaselecionada == 2: 
    nparcelas = int(input(f'Em quantas vezes você quer parcelar?'))

    if nparcelas == 1:
        cartão = preçobase
        valorparcela1 = cartão * 0.95
        print(f'O preço será de {valorparcela1} reais.')

    elif nparcelas == 2:
        cartão = preçobase
        cartão2x = cartão

        valorparcela2 = cartão2x / nparcelas
        print(f'O A parcela será de {valorparcela2}, totalizando {cartão2x} reais.')

    elif nparcelas >= 3:
        cartão = preçobase
        cartão3xmais = cartão * 1.2
        valorparcela3 = cartão3xmais / nparcelas
        print(f'O valor total será {cartão3xmais} reais, a parcela será de {valorparcela3} reais.')
else:
    print(f'Forma de pagamento inesistente')
