inicio = str(input('insira o nome de sua cidade.').strip())

#santo = inicio.lower() == 'santo'
santo = 'santo' in inicio.lower()

print(santo)