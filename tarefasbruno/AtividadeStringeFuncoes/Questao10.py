'''
Define uma função que retorna o valor de caractere P, se seu argumento for positivo, e
N, se seu argumento for zero ou negativo.
'''
def positivoounegativo(x):
    if x <= 0:
        return "N"
    else:
        return "P"

num1 = int(input("Digite um número para saber se é negativo ou positivo: "))
print(positivoounegativo(num1))