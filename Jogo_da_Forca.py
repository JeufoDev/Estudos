import regras
import os 

regras.regras_do_jogo()

palavra_chave = input("Digite a palavra para seu amigo acertar: ")
os.system('cls')
tamanho = len(palavra_chave)

palavra_secreta = ["-"] * tamanho
letras_testadas = []

chances = 5
ganhou = False

while chances>0 and ganhou == False:
    print(f"Você tem {chances} tentativa(s)")
    print(*palavra_secreta)

    opc = int(input("1- Testar a letra\n2- Tentar a palavra:\n"))
    if opc == 1:
        letra = input("\nDigite a letra para testar: ")
        if letra in letras_testadas or letra in palavra_secreta:
            chances-=1
            print(F"Que pena, repetiu a letra usada. Ainda tem {chances} tentativa(s)")
            print(f"Letras testadas {letras_testadas}")
        else:
            if letra in palavra_chave:
                print("Parabéns, acertou a letra!")
                for i in range(tamanho):
                    if letra == palavra_chave[i]:
                        palavra_secreta[i] = letra
                print(f"Letras testadas {letras_testadas}\n")
                if not "-" in palavra_secreta:
                    print("PARABÉNS, VOCÊ GANHOU!")
                    ganhou = True
            else:
                chances-=1
                print(F"Que pena, errou a letra. Ainda tem {chances} tentativa(s)")
                letras_testadas.append(letra)
                print(f"Letras testadas {letras_testadas}\n")
    elif opc == 2:
        palavra = input("Teste a palavra\n")
        if palavra == palavra_chave:
            ganhou = True
            regras.mostra_resultado(ganhou, palavra_chave, chances)
        else:
            chances = 0
            regras.mostra_resultado(ganhou, palavra_chave, chances)
    else:
        print("Opção inválida!")


regras.mostra_resultado(ganhou, palavra_chave, chances)
    