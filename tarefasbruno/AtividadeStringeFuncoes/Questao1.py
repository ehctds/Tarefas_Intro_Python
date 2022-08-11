'''
Faça um programa que leia duas strings e informe o conteúdo delas seguido do seu
comprimento. Informe também se as duas strings possuem o mesmo comprimento e são
iguais ou diferentes no conteúdo. 
'''


string1 = input("Informe a primeira String: ")
string2 = input("Informe a segunda String: ")
contador = 0
contador1 = 0
print(f"A string 1 é: {string1}")
print(f"A string 2 é: {string2}")

print(f"O tamanho da string 1 é: {(len(string1))}")
print(f"O tamanho da string 2 é: {(len(string2))}")

if (len(string1)) == (len(string2)):
    print("As strings possuem o mesmo tamanho")
else: 
    print("As strings não possuem o mesmo tamanho")

if string1 == string2:
    print("As strings possuem conteúdo igual")
else:
    print("As strings não possuem mesmo conteúdo")
