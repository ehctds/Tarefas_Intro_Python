'''
Faça um programa que leia números repetidamente até que o valor -1 seja digitado. Quando isso ocorrer, o programa deve 
exibir o menor valor, o maior valor e a soma dos valores.
'''

print("Digite -1 para sair do aplicativo.")
num= 0
soma=0
maiornumero= -9999999999999999999999999999999999999
menornumero= 99999999999999999999999999999999999999
while num != -1:
    num=float(input("Informe o valor: "))
    if num!= -1:
        soma= soma+num
        if maiornumero < num:
            maiornumero = num
        if menornumero > num:
            menornumero = num
if menornumero == 99999999999999999999999999999999999999:
    menornumero=0
if maiornumero== -9999999999999999999999999999999999999:
    maiornumero=0
print(f"O menor valor é {menornumero}") 
print (f"O maior valor é {maiornumero}")
print(f"A soma dos valores é {soma}")
print("Fim do Programa")
