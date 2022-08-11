'''
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o
nome do mês por extenso. 
'''

meses = {1: "janeiro", 2: "fevereiro", 3: "março", 4:"abril", 5:"maio", 6:"junho", 7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
data = input("Informe uma data: (dd/mm/aaaa) ")
if(data[2] !="/") or (data[5] !="/"):
    data = input("A data precisa estar no formato (dd/mm/aaaa): ")
data1 = data.split("/")
meseskeys = (list(meses.keys()))
data2 = int(data1[1])

for i in range(len(meseskeys)):
    if data2 == meseskeys[i]:
        data2 = meses[i+1]
        break

print(f"{data1[0]} de {data2} de {data1[2]}")