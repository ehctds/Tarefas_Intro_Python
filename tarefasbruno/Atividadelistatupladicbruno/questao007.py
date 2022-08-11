'''
Escreva um programa que leia frases, repetidamente, e que gere um dicionário para cada
frase lida. As chaves do dicionário serão os carateres digitados, e os valores devem 
consistir no número de vezes que o caractere aparece na frase. O programa deve exibir,
para cada frase, seu dicionário correspondente e ser encerrado quando o usuário digitar -1.
'''

dic = {}
lista= []
count = 0
count1 = 0 
continuar = 'sim'
contador = {}
while continuar != 'n':
    frase= input("Qual a frase ? ")
    for palavra in frase:
        lista.append(palavra)
    continuar = (input("Deseja continuar ? (n para parar) "))
for l in frase.lower():
    chaves = contador.keys()
    if l in chaves:
        contador[l] += 1
    else:
        contador[l] = 1
print(contador)
print(lista)
