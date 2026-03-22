n = str(input('Digite seu nome completo.'))

separador= n.split()
primeironome = separador[0]
ultimonome = separador[-1]

print(f'Seu primeiro nome é {primeironome} e o seu ultimo nome é {ultimonome}')