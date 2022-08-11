'''
Faça um programa que solicite ao usuário o turno que ele estuda, a partir dos caracteres a seguir:
M(matutino), V(verpertino) ou N(noturno). Depois disso, o programa deve exibir as mensagens "Bom dia!",
"Boa Tarde!", "Boa Noite!" ou "Valor Inválido!", conforme cada caso.
'''


turno = input("Qual turno você estuda ? (M) para matutino, (V) para vespertino, (N) para noturno ").lower()
if turno == "m":
    print("Bom Dia!")
elif turno == "v":
    print("Boa Tarde!")
elif turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")