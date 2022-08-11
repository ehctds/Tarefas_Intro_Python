'''
Faça um programa que leia dois vetores com cinco elementos cada e gere um terceiro vetor
de 10 elementos, cujo valores deverão ser compostos pelos elementos intercalados dos dois
outros vetores.
'''


vetor1= [None]*5
vetor2= [None]*5
vetor3 = []

for i in range(0,5):
    vetor1[i]= input(f" qual o elemento {i} do vetor 1 ? ")
    vetor2[i]= input(f" qual o elemento {i} do vetor 2 ? ")

for j in range(0,5):
    vetor3.append(vetor1[j])
    vetor3.append(vetor2[j])

print(f"o vetor 3 será {vetor3}")