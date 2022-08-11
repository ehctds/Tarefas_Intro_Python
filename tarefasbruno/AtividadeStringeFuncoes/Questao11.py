'''
Faça uma função que retorne a quantidade de dígitos de um determinado número inteiro
passado por parâmetro. 

'''

def quantdigint(x):
    count = 0
    for i in x:
        count += 1
    return count

num1 = input("Digite um número para saber a quantidade de dígitos: ")
print(quantdigint(num1))