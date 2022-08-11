'''
Implemente um programa que pergunte quanto um trabalhador ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para 
o sindicato. O programa deve exibir as seguintes informações:

salário bruto
quanto pagou ao INSS
quanto pagou ao sindicato 
o salário líquido
'''


salariohora = float(input("Qual é o seu salário por hora ? "))
horastrab = float(input("quantas horas você trabalha por mes ? "))
salariomensal = salariohora*horastrab
IR= salariomensal*0.11
INSS = salariomensal*0.08
Sindicato= salariomensal*0.05
salarioliquido = salariomensal- IR- INSS- Sindicato
print(f"Salário bruto: {salariomensal}")
print(f"IR(11%): {IR}")
print(f"INSS(8%): {INSS}")
print(f"Sindicato(5%): {Sindicato}")
print(f"Salário líquido: {salarioliquido}")
