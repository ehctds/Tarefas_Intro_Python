'''
Escreva um programa que leia dois números e imprima o resultado da divisão inteira do
primeiro pelo segundo, assim como o resto da divisão, usando o comando while e o
operador aritmético de subtração. Lembre-se que podemos entender o quociente da
divisão de dois números como a quantidade de vezes que podemos retirar o divisor do
dividendo. Logo, 20 ÷ 4 = 5, pois podemos subtrair 4 cinco vezes de 20. 
'''


num1 = int(input("Qual o primeiro número ? "))
num2 = int(input("Qual o segundo número ? "))
x= num1
count = 0
while x >= num2:
    x = x - num2
    count = count + 1
resto = x
print(f" O resultado da divisão é {count} e o resto é {resto} ")