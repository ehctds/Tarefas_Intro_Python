'''
Escreva um programa que leia um número e verifique se ele é primo. Para fazer essa
verificação, calcule o resto da divisão do número informado por todos os número menores
que ele a partir de 2. Se o resto de uma dessas divisões for igual a 0, o número não é
primo. Note que 0 e 1 não são primos e que 2 é o único primo que é par. 
'''

num = int(input("Qual o numero ? "))
div = 0
for i in range(num):
    if i >= 2:
       div = num % i
if div == 0 and num!=2:
    print("O número não é primo")
else:
    print("O número é primo")