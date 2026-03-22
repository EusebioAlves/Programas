frase = 'Aprendendo a programar em Pythons'
#print(frase[3]) #caractere na posição 3
#print(frase[3:5]) #Caracteres entre 3 e 5 (5 é desconsiderado)
print(frase[1:5]) #sem começo até 5
#print(frase[5:]) #inverso da de cima
#print(frase[1:10:2]) #o "2" pula de 2 em 2

#---------------funções----------------------

#print(frase.count('a'))
#print(frase.upper().count('a'))
print(len(frase.lstrip())) #strip desconsidera os espaços "r" e "l"

#frase = frase.replace(frase,'Aprendido') #-----ATRIBUI FRASE PARA REPLACE ("frase = ...")
#print(frase)

#print(frase.lower().find('aprendendo')) # transforma em minusculo para achar digitando minusculo e "find" acha o que está em () e diz a posição

#frase = frase.split() #separa as frases
#print(frase[2][2]) #o primeiro [2] é a frase 3 o segundo [2] é a posição da letra, que retorna a letra
 