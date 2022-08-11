'''
Faça um programa que exiba na tela o número de ocorrências de cada caractere de uma
frase digitada pelo usuário. A contagem dos caracteres deve ocorrer dentro de uma função
que recebe uma string por parâmetro e retorna um dicionário cuja chave é o próprio
caractere e o valor corresponde ao número de vezes que ele aparece na string. 

'''


dic = {}
lista= []
contador = {}
frase= input("Qual a frase ? ")
for palavra in frase:
    lista.append(palavra)
for l in frase.lower():
    chaves = contador.keys()
    if l in chaves:
        contador[l] += 1
    else:
        contador[l] = 1
print(contador)