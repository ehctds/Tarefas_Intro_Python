'''
Escreva um programa que leia as coordenadas de N pontos do plano cartesiano e que
exiba as distâncias mínima, máxima e média entre esses pontos. O programa deve
representar os pontos como uma lista de tuplas e deve adotar a distância euclidiana
para aferir a distância dentre dois pontos.
'''

num = int(input("Quantos Pontos serão calculados ? "))
lista = []
lista2 = []
maiornum = -9999999999
menornum = 9999999
soma = 0
for i in range(num):
    A= int(input("Qual a primeira coordenada do primeiro ponto ? "))
    A1= int(input("Qual a segunda coordenada do primeiro ponto ? "))
    tupla = (A,A1)
    lista.append(tupla)
    B = int(input("Qual a coordenada do segundo ponto ? "))
    B1= int(input("Qual a segunda coordenada do segundo ponto ? "))
    tupla2 = (B,B1)
    lista.append(tupla2)
    DistanciaEucli = ((B-A)**2 + (B1- A1)**2)**0.5
    soma += DistanciaEucli
    lista2.append(DistanciaEucli)
print(lista)
print(lista2)
media = soma/len(lista2)
for i in range(num):
    if lista2[i] > maiornum:
        maiornum= lista2[i]
    if lista2[i]<menornum:
        menornum= lista2[i]
print(maiornum)
print(menornum)
print(media)
