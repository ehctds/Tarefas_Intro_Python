'''
Duas amigas estabelerecam o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
Cada letra equivale a um número entre 1 e 26, e o espaço ao 0. Faça um programa que receba como entrada
uma lista de números representando uma mensagem codificada, armazene estes valores em uma lista e depois traduza
a mensagem de acordo com o código das amigas.
'''

codigo= {0:' ', 1: "a" , 2: "b", 3: "c", 4: "d", 5:"e", 6:"f" , 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 
14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20:"t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}

num=0
mensagem = []
stop = "s"
while stop != "n":
    num= int(input("Qual numero você deseja traduzir ? "))
    if num >= 0 and num <= 26:
        mensagem.append(num)
    else:
        print("Número Inválido")
    stop= input("Deseja continuar ? (para parar digite n) ")

print(mensagem)

for i in range(0,len(mensagem)):
    print(codigo[mensagem[i]])