import os
os.system('cls')

nome = str(input('insira o nome do aluno.').strip())

nota1 = float(input('insira a primeira nota.'))
nota2 = float(input('insira a segunda nota.'))
nota3 = float(input('insira a terceira nota.'))
nota4 = float(input('insira a quarta nota.'))

listanotas = [nota1,nota2,nota3,nota4]

somanotas = sum(listanotas)
qtdfatores = len(listanotas)
média = somanotas/qtdfatores
metamédia = 7

if média >= metamédia:
    print(f'O aluno {nome} obteve média {média:.2f}. Portanto, ele está aprovado!')
else:
    print(f'O aluno {nome} obteve média {média:.2f}. Portanto, ele está reprovado!')