'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de
eleitores, leia os votos consistindo nos números dos candidatos (você define tais números)
e, ao final, exiba o número de votos de cada um recebeu. 

'''

candt1= 0
candt2 = 0
candt3= 0
nulo= 0
neleitores= int(input("Quantos eleitores são ? "))
for neleitores in range(neleitores):
    voto = int(input("Digite o número do seu candidato: "))
    if voto == 1:
        candt1 += 1
    elif voto == 2:
        candt2 += 1
    elif voto == 3:
        candt3 += 1
    else:
        nulo += 1
        print("Voto inválido")
print(f"O candidato 1 recebeu {candt1} votos")
print(f"O candidato 2 recebeu {candt2} votos")
print(f"O candidato 3 recebeu {candt3} votos")
print(f"Houve {nulo} votos nulo")