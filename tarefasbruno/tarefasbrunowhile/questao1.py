'''
Escreva um programa que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500. 
'''

x=1
soma=0
while (x<=498):
    x=x+2
    resto = x%3
    if resto==0:
        soma= soma+x
        print(x)
print(soma)