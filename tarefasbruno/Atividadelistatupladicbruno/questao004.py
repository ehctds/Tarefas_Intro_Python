'''
Escreva um programa em Python que simula o lançamento de um dado n vezes e imprime
o percentual de surgimento de cada face do dado. O valor n é introduzido pelo usuário,
sendo que zero encerra o programa. Seu programa deverá utilizar um array para armazenar 
os números de aparecimento de cada face.
'''


import random
num = 1
lista = []
num1 = 0
num2= 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
while num != 0:
    print("Girando o dado !")
    dado=random.randint(1,6)
    print(f"Caiu no número {dado}")
    lista.append(dado)
    print(lista)
    num= int(input("Deseja continuar ? (digite 0 para parar) "))
for i in range(len(lista)):
    if lista[i]==1:
        num1 += 1
    elif lista[i]==2:
        num2 += 1
    elif lista[i]==3:
        num3 += 1
    elif lista[i]==4:
        num4 += 1
    elif lista[i]==5:
        num5+= 1
    elif lista[i]==6:
        num6 += 1
num1 = (num1/len(lista)) * 100
num2 = (num2/len(lista)) * 100
num3 = (num3/len(lista)) * 100
num4 = (num4/len(lista)) * 100
num5 = (num5/len(lista)) * 100
num6 = (num6/len(lista)) * 100

print(f"A porcentagem de vezes que apareceu o número 1 no dado foi {num1}%")
print(f"A porcentagem de vezes que apareceu o número 2 no dado foi {num2}%")
print(f"A porcentagem de vezes que apareceu o número 3 no dado foi {num3}%")
print(f"A porcentagem de vezes que apareceu o número 4 no dado foi {num4}%")
print(f"A porcentagem de vezes que apareceu o número 5 no dado foi {num5}%")
print(f"A porcentagem de vezes que apareceu o número 6 no dado foi {num6}%")