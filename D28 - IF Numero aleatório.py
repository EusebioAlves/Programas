#jogo da adivinhação de numeros, de 1-5
import random
import os

naleatorio = random.randint(1,5)
    
while True:

    os.system('cls')

    variaveis = input('Tente adivinhar um numero, entre 1 e 5, que eu estou pensando').strip().lower()    
    

    if variaveis == 'sair':
        print('fechando o sistema...')
        break #quebra o loop e para tudo
    
    num = int(variaveis)


    if num == naleatorio:
        print(f'Você acertou! Eu pensei no numero {naleatorio}')
        input('Pressione "enter" para reiniciar')
        
    

    elif num != naleatorio:
        print(f'Você errou! Eu pensei no numero {naleatorio}')
        input('Pressione "enter" para reiniciar')
        
        


