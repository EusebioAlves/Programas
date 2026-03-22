import os
os.system('cls')

#Peça o nome completo de uma pessoa. 
#O programa deve montar um e-mail institucional seguindo este padrão: 
# primeironome.ultimonome@empresa.com.br.

nome = str(input('Digite seu nome completo.').strip().lower())

formaton = nome.split()
pnome = formaton[0]
unome = formaton[-1]
arrobaempresa = '@dex.co'
emailformado = f'{pnome}{unome}{arrobaempresa}'

print(f'Email formado: {emailformado}')
