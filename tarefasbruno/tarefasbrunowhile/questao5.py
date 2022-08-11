'''
Implemente um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago. Exiba na tela o número de meses em que
a dívida será paga, o total pago e o total de juros pago. 
'''

valor_inicial = float(input("Qual o valor da sua dívida ? "))
juros= (float(input("Qual a taxa de juros ? ")))/100
valor_mensal = int(input("Qual valor por mês que você deseja pagar ? "))
meses= 0
valorjuros= 0
while valor_inicial > 0:
    valorjuros= (((valor_inicial)+(valor_inicial*juros))-valor_inicial) + valorjuros
    valor_inicial= ((valor_inicial)+(valor_inicial*juros)) - (valor_mensal)
    meses+=1
valor_final= (valor_mensal*meses)-(-valor_inicial)
print(F"a dívida será paga em {meses} meses")
print(F"O valor final pago será: {valor_final}")
print(F"O total de juros pago foi: {valorjuros}")
