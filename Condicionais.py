#Estrutura
import os
os.system('cls')

n = int(input('Digite sua idade'))

if n >= 60:
    print('Você é um idoso.')
elif n >= 18:
    print('Você já é adulto.')
elif n >= 12:
    print('Você é um adolescente.')
else: 
    print('Você é uma criança.')

