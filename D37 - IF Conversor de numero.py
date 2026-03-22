import os 
os.system('cls')

n = int(input('Digite um número inteiro.'))

print('''Escolha uma das 3 opções:'
1-binário
2-Octal'
3- hexadecimal''')

if n == 1:
    print(f'O número {n} em binário é {bin(n)}')
elif n == 2:
    print(f'O número {n} em Octal é {oct(n)}')
elif n == 3:
    print(f'O número {n} em hexadecimal é {hex(n)}')
else:
    print('número inválido.')