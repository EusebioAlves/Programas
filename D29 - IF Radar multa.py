import os
os.system('cls')

v = float(input('Velocidade registrada.'))

limitevel = 80
vexcedente = v - limitevel
valormulta = 7 * vexcedente
    
if v <= limitevel:
    print('Velocidade nos conformes')
else:
    print(f'Acima da velocidade permitida! A multa é de {valormulta}')