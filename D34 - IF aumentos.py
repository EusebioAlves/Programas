# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

import os
os.system('cls')


sal = float(input('Qual o valor do seu salário?'))
valacima1250 = 1.1
valabaixo1250 = 1.15

if sal > 1250:
    aumento1 =  sal * valacima1250
    variação1 = aumento1 - sal
    percentilaumento1 = ((valacima1250 *100) -100)
    print(f'O seu salário de {sal:.2f} terá um aumento de {percentilaumento1:.2f}%. Acrescentado {variação1:.2f}R$. O total será {aumento1:.2f}R$.')

elif sal <= 1250:
    aumento2 =  sal * valabaixo1250
    variação2 = aumento2 - sal
    percentilaumento2 = ((valacima1250 *100) -100)
    print(f'O seu salário de {sal:.2f} terá um aumento de {percentilaumento2:.2f}%. Acrescentado {variação2:.2f}R$. O total será {aumento2:.2f}R$.')  