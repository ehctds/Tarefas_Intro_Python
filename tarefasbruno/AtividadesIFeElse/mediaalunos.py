'''
Desenvolva um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um 
semestre, calcule a sua média e exiba seu conceito de acordo com a tabela de aproveitamento.
'''

nota1 = float(input ("Qual a sua primeira nota ? "))
nota2= float(input ("Qual a sua segunda nota ? "))
medianota= (nota1+nota2)/2
if medianota >=9:
    print(F"sua média foi {medianota} e seu Conceito foi= A")
elif medianota >=7.5:
    print(F"sua média foi {medianota} e seu Conceito foi= B")
elif medianota >=4.0:
    print(F"sua média foi {medianota} e seu Conceito foi= C")
else:
    print(F"sua média foi {medianota} e seu Conceito= E")
