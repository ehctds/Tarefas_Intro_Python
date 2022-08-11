'''
Desenvolva um jogo da forca. O programa terá uma lista de palavras como entrada e
escolherá uma aleatoriamente. O jogador poderá errar seis vezes antes de ser enforcado. 

'''

import random
palavra = ["BRUNOGOL","EDGARD", "PYTHON", "PROGRAMACAO" ]
sorteio = random.randint(0, 3)
palavraescolhida = palavra[sorteio]
digitadas = []
chances = 6
while True:
    letra = input("Digite uma letra: ")
    digitadas.append(letra.upper())
    letrasacertadas = "" 
    for letratentativa in palavraescolhida:
        if letratentativa in digitadas:
            letrasacertadas += letratentativa
        else:
            letrasacertadas += "_"
        
    if letrasacertadas==palavraescolhida:
        print("Você venceu o jogo")
        break
    else: 
        print(f"A forca está assim {letrasacertadas}")
        
    if letra.upper() not in palavraescolhida:
        chances -= 1
        print(f" você tem {chances} chances restantes")
    
    if chances <= 0:
        print("Você Perdeu")
        break
