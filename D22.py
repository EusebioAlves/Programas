nc = str(input('Digite seu nome completo.'))

nmaiusculo = nc.upper()
nminusculo = nc.lower()
qtdletras = len(nc.replace(' ',''))
qtd1nome = len(nc.split()[0])

print(f'nome todo mauisculo {nmaiusculo}')
print(f'nome todo minusculo {nminusculo}')
print(f'Quantidade de caracteres (sem espaços) é {qtdletras}')
print(f'Qtd de letras no primeiro nome {qtd1nome}')
