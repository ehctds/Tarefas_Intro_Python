'''
Escreva um programa que solicite ao usuário que digite um número de 1 a 99 e imprima-o
na tela por extenso. 
'''

num = int(input("Digite um número de 1 a 99: "))

numeros = {1:"Um",2:"Dois",3:"Três",4:"Quatro",5:"Cinco",6:"Seis",7:"Sete",8:"Oito",9:"Nove",10:"Dez",11:"Onze",12:"Doze",13:"Treze",14:"Catorze",
15:"Quinze",16:"Dezesseis",17:"Dezessete",18:"Dezoito",19:"Dezenove",20:"Vinte",30:"Trinta",40:"Quarenta",50:"Cinquenta",60:"Sessenta",70: "Setenta",80:"Oitenta",90:"Noventa"}

if num >= 21 and num <= 29:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[20]} e {numeros[num3].lower()}")

elif num >= 31 and num <= 39:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[30]} e {numeros[num3].lower()}")
    
elif num >= 41 and num <= 49:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[40]} e {numeros[num3].lower()}")

elif num >= 51 and num <= 59:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[50]} e {numeros[num3].lower()}")

elif num >= 61 and num <= 69:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[60]} e {numeros[num3].lower()}")

elif num >= 71 and num <= 79:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[70]} e {numeros[num3].lower()}")

elif num >= 81 and num <= 89:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[80]} e {numeros[num3].lower()}")

elif num >= 91 and num <= 99:
    num1 = str(num)
    for i in num1:
        num3 = int(i)
    print(f"{numeros[90]} e {numeros[num3].lower()}")

else:
    print(numeros[num])