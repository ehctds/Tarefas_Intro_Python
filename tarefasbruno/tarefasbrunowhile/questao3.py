'''
Supondo que a população de um país X seja da ordem de 70.000 habitantes com uma taxa
anual de crescimento de 3.5% e que a população de Y seja 180.000 habitantes com uma
taxa de crescimento de 1.5%. Escreva um programa que calcule e escreva o número de
anos necessários para que a população do país X ultrapasse ou iguale a população do país
Y, mantidas as taxas de crescimento. 
'''

X= 70000 
Y= 180000 
Anos = 0
while X<=Y:
    X= (X + (0.035*X))
    Y= (Y + (0.015*Y))
    Anos= Anos + 1
print(F"Em {Anos} anos o país X ultrapassará o país Y")