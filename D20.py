import random
n1 = str(input('Nome 1'))
n2 = str(input('Nome 2'))
n3 = str(input('nome 3'))


ordemt = [n1,n2,n3]
random.shuffle(ordemt)

print(f'A ordem é {ordemt}.')