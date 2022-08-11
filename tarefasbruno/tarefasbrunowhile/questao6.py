'''
Desenvolva um programa para simular um simples sistema de vendas. Você deve solicitar
ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de
códigos abaixo a seguir para obter o preço da cada produto. 
Código Preço
1  5,50
2  2,30
3  4,75
4  6,80
5  9,30 
O programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro
código deve gerar a mensagem de erro “Código inválido”. 
'''


codigo=int(input("Qual o código do produto ? "))
valor=0
quantidade = 0
while codigo != 0:
    if codigo== 1:
        quantidade= int(input("Quantidade comprada: "))
        valor= 5.50*quantidade+ valor
    elif codigo== 2:
        quantidade= int(input("Quantidade comprada: "))
        valor= 2.30*quantidade+ valor
    elif codigo== 3:
        quantidade= int(input("Quantidade comprada: "))
        valor= 4.75*quantidade+ valor
    elif codigo== 4:
        quantidade= int(input("Quantidade comprada: "))
        valor= 6.80*quantidade+ valor
    elif codigo== 5:
        quantidade= int(input("Quantidade comprada: "))
        valor= 9.30*quantidade+ valor
    else:
        print("Código inválido")
    codigo=int(input("Qual o código do produto ? "))
print(f"o valor total da compra foi {valor}")