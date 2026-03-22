import random

n1 = str(input('nome 1'))
n2 = str(input('nome 2'))
n3 = str(input('nome 3'))

lista = [n1,n2,n3]

random.shuffle(lista)

print(f'A ordem é {lista}.')