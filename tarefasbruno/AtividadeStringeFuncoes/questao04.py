'''
Escreva um programa que elimina os brancos de uma string digitada pelo usuário.

'''

string1 = input("Qual frase você deseja remover os espaços ? ")
string2 = string1.replace(" ", "")
print(string2)


#2 método 
'''
string = input("Qual frase você deseja remover os espaços ? ")
string2 = string.split()
for i in range (len(string2)):
    print(string2[i],end = "")
print()

'''