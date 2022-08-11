'''
No século XIII, o matemático Leonardo Pisa, conhecido como Fibonacci, propôs a seguinte
sequência: (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...). Essa sequência tem uma lei de formação
simples; cada elemento, a partir do terceiro, é obtido somando-se os dois anteriores. Veja:
1+1=2, 2+1=3, 3+2=5 e assim por diante. Faça um programa que leia um número inteiro n
e exiba na tela a sequência de Fibonacci com n elementos. 
'''

numseq = int(input('Quantos termos ? '))
num1 = 0
num2 = 1
fib = 0
for i in range(numseq):
    if (i%2)==0:
        num1 = fib
    if (i%2)==1:
        num2 = fib
    fib = num1 + num2
    print(fib)