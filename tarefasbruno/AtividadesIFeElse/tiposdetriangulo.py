'''
Escreva um programa que leia como entrada os três lados de um triângulo, classifique o triângulo em
equilátero, isósceles ou escaleno, e exiba na tela sua classificação.
'''


lado1= float(input("Qual o primeiro lado do trianqulo ? "))
lado2= float(input("Qual o segundo lado do trianqulo ? "))
lado3= float(input("Qual o terceiro lado do trianqulo ? "))
if lado1==lado2 and lado2==lado3:
    print("O triângulo é equilátero")
elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    print("O triângulo é isósceles")
else: 
    print("O triângulo é escaleno")