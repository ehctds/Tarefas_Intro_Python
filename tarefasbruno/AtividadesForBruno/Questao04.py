'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem. 
'''

potencia=1
base= int(input("Qual a base ? "))
expoente= int(input("Qual o expoente ? "))
for i in range(expoente):
    potencia *= base
print(f"{base}^{expoente} = {potencia}")