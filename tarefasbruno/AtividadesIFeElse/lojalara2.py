'''
Passados seis meses, a loja de lara teve um crescumento surpreendente e agora ela vai aceitar pagamentos também com cartão.
O cliente poderá escolher entre as funções débito e crédito, e ainda parcelar sua compra em até 3 vezes na opção crédito.
Modifique o programa anterior para que as novas formas de pagamento sejam consideradas e, além do valor final a ser pago,
seja exibido o valor de cada parcela nas compras com cartão de crédito.
'''

valorproduto = float(input("Qual o valor do produto ? "))
formadepagamento= (input("Qual a forma de pagamento ? (Cartão, Cheque, Dinheiro) ")).lower()
if formadepagamento == "cartão":
    creditooudebito= (input("Crédito ou débito ? ")).lower()
    if creditooudebito== "crédito":
        valordeparcelas= int(input("quantas parcelas ? "))
        if 1<=valordeparcelas<=3:
            valorprodutoparcelado= valorproduto/valordeparcelas
            print(f"Serão {valordeparcelas}x parcelas de {valorproduto} que vai dar {valorprodutoparcelado} reais por parcela")
        if valordeparcelas>3:
            print("Número de parcelas inválido")
    if creditooudebito== "débito":
        print(f"O valor do produto é {valorproduto}")       
elif 0 <valorproduto< 100 and (formadepagamento == "dinheiro" or "cheque"):
    print(f"O valor do produto é {valorproduto}")
elif valorproduto >= 100 and formadepagamento=="dinheiro":
    valorproduto = (valorproduto)- valorproduto*0.1
    print(f"O valor do produto -10% de desconto é: {valorproduto}")
elif valorproduto >= 100 and formadepagamento== "cheque":
    print(f"O valor do produto é {valorproduto}")
else: 
    print("Valor do produto ou Forma de pagamento inválida")