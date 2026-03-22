import os
os.system('cls')

altura = float(input('Informe sua altura em m.').replace(',','.'))
peso = float(input('informe sua massa corporal em kg.').replace(',','.'))

imc = peso/(altura**2)

if imc < 18.5:
    print(f'Essa pessoas se classifica no grupo "Magreza". Seu imc é de {imc}')
elif imc <= 24.9:
    print(f'Essa pessoas se classifica no grupo "Normal". Seu imc é de {imc}.')
elif imc <= 29.9:
    print(f'Essa pessoas se classifica no grupo "Sobrepeso". Seu imc é de {imc}')
else:
    print(f'Essa pessoas se classifica no grupo "Obeso". Seu imc é de {imc}')