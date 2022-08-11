'''
Faça um programa que peça para 𝑛 pessoas a sua idade, ao final o programa deverá
verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 
'''

idadetotal= 0
npessoas= int(input("Quantas pessoas são ? "))
for npessoas in range(npessoas):
    idade= int(input("Digite a idade da pessoas: "))
    idadetotal += idade
media= idadetotal/npessoas
if media<=25:
    print("A turma é jovem")
elif media<= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")