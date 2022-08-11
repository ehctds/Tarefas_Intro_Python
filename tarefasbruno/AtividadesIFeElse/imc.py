'''
Crie um programa que tenha como entrada a altura (h) de uma pessoa, e calcule
e exiba seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7*h)-58
Para mulheres: (62.1*h)-44.7
'''

altura= float(input("Qual a sua altura em metros ? "))
genero = input("qual o seu gênero ? (homem ou mulher) ").lower()
if genero == "homem":
    pesoideal = (72.7*altura)-58
    print(f"O seu peso ideal é {pesoideal}")
elif genero== "mulher":
    pesoideal = (62.1*altura)-44.7
    print(f"O seu peso ideal é {pesoideal}")
else:
    print("Género inválido")
