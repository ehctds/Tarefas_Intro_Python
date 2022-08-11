'''
Lara abriu uma loja de bijuterias recentemente, e as vendas vão muito bem. Pensando em atrair uma clientela ainda maior,
ela deseja oferecer um desconto de 10% para os clientes que gastarem 100 ou mais e pagarem em dinheiro. Escreva um programa
que receba como entrada o valor do produto comprado e a forma de pagamento escolhida (dinheiro ou cheque), calcule o desconto
devido (caso necessário) e exiba o valor final a ser pago.
'''


valorproduto = float(input("Qual o valor do produto ? "))
formadepagamento= (input("Qual a forma de pagamento ? (Cheque ou dinheiro) ")).lower()

if 0 <valorproduto< 100 and (formadepagamento == "dinheiro" or "cheque"):
    print(f"O valor do produto é {valorproduto}")
elif valorproduto >= 100 and formadepagamento=="dinheiro":
    valorproduto = (valorproduto)- valorproduto*0.1
    print(f"O valor do produto -10% de desconto é: {valorproduto}")
elif valorproduto >= 100 and formadepagamento== "cheque":
    print(f"O valor do produto é {valorproduto}")
else: 
    print("Valor do produto ou Forma de pagamento inválida")