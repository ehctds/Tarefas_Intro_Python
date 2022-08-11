'''
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros
no período.
'''

depositoinicial= int(input("Quanto foi depositado ? "))
deposito= depositoinicial
juros= int((input("Quanto é a taxa de juros ? ")))/100
for i in range (1,25):
    ganho_mensal= depositoinicial*juros
    depositoinicial= depositoinicial+(ganho_mensal)
    print(depositoinicial)
    print(ganho_mensal)
depositofinal= depositoinicial- deposito
print(f"o total ganho com juros foi {depositofinal}")