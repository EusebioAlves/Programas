import os
os.system('cls')

print('Simulador de emprestimos')

valorcasa = float(input('Digite o valor da casa para o emprestimo.'))
salario = float(input('Informe seu salário mensal.'))
tempoapagar = float(input('Em quantos anos pretende pagar?'))
anoparames = tempoapagar*12

parcela = valorcasa/anoparames

if parcela <= 0.3 * salario:
    print(f'Emprestimo aprovado. A parcela será de {parcela} Reais.')

if parcela >= 0.3 * salario:
    print(f'Emprestimo reprovado. A pois a parcela será de {parcela} Reais.')