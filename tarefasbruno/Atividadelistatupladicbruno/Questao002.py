'''
Crie um programam que leia uma matriz 3x3 e troque os elementos da linha 2 pela coluna 2 
e vice-versa.
'''


colunamatriz=[]
matriz = []
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(int(input("Qual o numero ? ")))
    matriz.append(linha)
colunamatriz = matriz[1]+ colunamatriz

#print(colunamatriz)
print(matriz)

for k in range(0,3):
    matriz[1][k]= matriz[k][1]

for g in range(0,3):
    matriz[g][1]=colunamatriz[g]

#print(colunamatriz)
print(matriz)
