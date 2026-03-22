import os
os.system('cls')


n1 = float(input('Digite um número.'))
n2 = float(input('Digite outro número.'))
n3 = float(input('Digite mais um número.'))

lista = [n1,n2,n3]

valormaximo = max(lista)
valorminimo = min(lista)
somavalor = sum(lista)
qtdfatores = len(lista)
média = somavalor/qtdfatores


print(f'Valor máximo é {valormaximo}')
print(f'Valor minimo é {valorminimo}')
print(f'A soma de todos os números é {somavalor}')
print(f'A quantidade de numeros é {qtdfatores}')
print(f'A média é {média:.2f}')