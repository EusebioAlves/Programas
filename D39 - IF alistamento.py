import os 
os.system('cls')

from datetime import date

anoatual = date.today().year

anonascimento = int(input('Seu ano de nascimento'))

idade = anoatual - anonascimento

anoapresentação = anonascimento + 18

passadoalistamento = idade - 18
print(passadoalistamento)


if (anoatual - anonascimento) > 18:
    print(f'Essa pessoa deveria ter se alistado em {anoapresentação}, há {passadoalistamento} anos atrás.')
elif (anoatual - anonascimento) < 18:
    print(f'Essa pessoa deverá se alistar em {anoapresentação}, daqui há {passadoalistamento} anos.')
else:
    print(f'Essa pessoas está apta a se alistar nesse ano.')