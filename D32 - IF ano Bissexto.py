import os
os.system('cls')

import datetime

ano = int(input('Digite um ano qualquer.'))

#bissexto = ano % 4 and ano % 400 or ano % 100

if  ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    print(f'Esse ano é Bissexto!')
else:
    print('Esse ano não é bissexto.')