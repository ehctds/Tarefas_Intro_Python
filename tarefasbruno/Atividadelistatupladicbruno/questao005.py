'''
Suponha que se deseje processar um conjunto de valores representando altura e sexo(M/F)
de um grupo de 10 pessoas. Escreva um programa em Python que:

(A) leia este conjunto de dados e armezene-o em duas listas vinculadas, uma das quais 
contém as alturas e a outra contém os sexos dos indivíduos.

(B) Determine a maior e a menor altura dentre esses indivíduos, indicando o sexo do
indivíduo de maior altura e o sexo do indivíduo de menor altura.

(C) Encontre a média de altura entre os indivíduos do sexo feminino (representados no programa
pelo cartere 'F') e a média de altura entre os indivíduos do sexo masculino (representados no
programa pelo caratere 'M')

(D) Determine o número total de indivíduos de cada sexo.
'''



count = 0
alturamasculina= 0
alturafeminina = 0
mediaalturamasculina= 0
mediaalturafemina = 0
count1 = 0
tabela = [([None]*10),([None]*10)]
maioraltura = 0
menoraltura = 2700
for i in range(0,10):
    tabela[0][i] = int(input(f"Qual a altura do(a) {i+1} em centímetros ? "))
    tabela[1][i] = (input(f"Qual o sexo do(a) {i+1} ? (M ou F) ")).upper()
    if tabela[0][i] > maioraltura:
        sexomaioraltura = tabela[1][i]
        maioraltura = tabela[0][i]
    if tabela[0][i] < menoraltura:
        sexomenoraltura= tabela[1][i]
        menoraltura= tabela[0][i]
    if tabela[1][i] == "F":
        count += 1
        alturafeminina= alturafeminina + tabela[0][i]
        mediaalturafemina= alturafeminina/count
    else:
        count1 += 1
        alturamasculina = alturamasculina + tabela[0][i]
        mediaalturamasculina= alturamasculina/count1

print(f" A maior altura foi {maioraltura} e o sexo é {sexomaioraltura}")
print(f" A menor altura foi {menoraltura} e o sexo é {sexomenoraltura}")
print(f" A média de altura feminina foi {mediaalturafemina}")
print(f"A média de altura masculina foi {mediaalturamasculina}")
print(f"A quantidade de mulheres foi {count}")
print(f"A quantidade de homens foi {count1}")
