'''
Desenvolva um programa que solicite a digitação de um número de CPF no formato
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos
verificadores dos caracteres de formatação

'''

cpfRecebido1= str(input("Digite o cpf no formato xxx.xxx.xxx-xx: "))
cpfRecebido2 = cpfRecebido1.replace(".","")
cpfRecebido = str(cpfRecebido2.replace("-",""))
cpf = []
for i in cpfRecebido:
    cpf.append(int(i))
cpfInvalido = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']
resultadoSomaPDV = 0
resultadoMultiplicacaoPDV = 0
resultadoSomaSDV = 0
resultadoMultiplicacaoSDV = 0
situacao = False

for i in range(0, 9):
    resultadoMultiplicacaoPDV = cpf[i] * (10 - i)
    resultadoSomaPDV = resultadoSomaPDV + resultadoMultiplicacaoPDV

resultadoRestoPDV = resultadoSomaPDV % 11
pdv = 0 if resultadoRestoPDV >= 10 else (11 - resultadoRestoPDV)

for i in range(0, 10):
    resultadoMultiplicacaoSDV = cpf[i] * (11 - i)
    resultadoSomaSDV = resultadoSomaSDV + resultadoMultiplicacaoSDV

resultadoRestoSDV = resultadoSomaSDV % 11
sdv = 0 if resultadoRestoSDV >= 10 else (11 - resultadoRestoSDV)

for i in range(0, 10):
    if cpfRecebido == cpfInvalido[i]:
        situacao = True
        break
    else:
        situacao = False

if(situacao):
    print('CPF invalido')
elif (cpf[9] == pdv) and (cpf[10] == sdv):
    print('CPF válido')
else:
    print('CPF inválido')