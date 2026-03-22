#exercicio 2
import os
os.system('cls')

q = str(input('Digite algo').strip().lower())

contE = q.count('e')
pi = q.find('e')
pf = q.rfind('e')


print(f'Essa palavras em quantos "E"? {contE}')
print(f'Qual é a posição do primeiro "E"? {pi}')
print(f'Qual é a posição do ultimo "E"? {pf}')