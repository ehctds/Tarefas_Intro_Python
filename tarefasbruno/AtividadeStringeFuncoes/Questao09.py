'''
Escreva uma função que receba três argumentos (parâmetros) e retorne sua soma. Escreva
um programa para testá-la.

'''

def soma (x,y,z):
    soma = x+y+z
    return soma

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(f"a soma de {num1} + {num2} + {num3} resultará em {soma(num1,num2,num3)}")