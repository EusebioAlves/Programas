num = int(input('Digite um numero até 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'milhar {m}, centena {c},dezena {d}, unidade {u}')