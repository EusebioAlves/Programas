cidade = str(input('Digite o nome de uma cidade.'))

cmaius = cidade.upper()
qtdletras = len(cidade.replace(' ',''))
vsão = 'são' in cidade.lower()

print(f'Tudo maiusculo:{cmaius}')
print(f'A quantidade de letras é: {qtdletras}')
print(f'Tem São? {vsão}')