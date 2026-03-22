import os
os.system('cls')
import math

n = int(input('Digite um número.'))

divisão = n % 2

if divisão == 1:
    print('Esse numero é impar.')
else:
    print('Esse numero é par.')
print(divisão)