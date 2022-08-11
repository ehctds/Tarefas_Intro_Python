'''
Escreva um programa em Python que receba uma string e a imprima na vertical e em
formato de escada. Por exemplo, se o usuário digitar a string FULANO, o programa deve
exibir a seguinte saída:
F
FU
FUL
FULA
FULAN
FULANO

'''

string = str(input('Digite a string: '))
for i in range(0,len(string)+1):    
    print(string[:i])