import os
os.system('cls')

idade = int(input('Informe sua idade.'))

if idade <= 9:
    print('Esse atleta pertence a categoria Mirim.')
elif idade <= 14:
    print('Esse atleta pertence a categoria infantil.')
elif idade <= 19:
    print('Esse atleta pertence a categoria Júnior.')
elif idade <= 25:
    print('Esse atleta pertence a categoria Sênior.')
else:
    print('Esse atleta pertence a categoria Master')