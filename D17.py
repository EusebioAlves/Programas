import math

ang = float(input('Digite um angulo').replace(',','.'))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print(f'O seno, o cosseno e a tangente desse angulo é respectivamente: {sen}, {cos} e {tg}')
                  

