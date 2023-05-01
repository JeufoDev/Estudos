#PÁGINA PARA ENSINAS AS REGRAS AO PARTICIPANTE
import os

def regras_do_jogo():
    print("-"*50)
    print("seja bem vindo ao Jogo da forca!!".upper())
    print("Regras:\n1- O jogador tem apenas 5 pontos para errar\n2- Se digitar letra que já foi usada gasta uma chance\n3- O jogador pode tentar acertar a palavra, mas se errar perde o jogo")
    print("Que comecem os jogos!".upper())
    print("-"*50)
   
def mostra_resultado(valor, palavra, chances):
    os.system('cls')
    if valor == False:
        print(f"Você perdeu!\nA palavra era {palavra}")
    else:
        print(f"Você ganhou!\nE ainda tinha {chances} tentativ(s), a palavra era {palavra}")