import regras
import os 

regras.regras_do_jogo()

palavra_chave = input("Digite a palavra para seu amigo acertar: ")
os.system('cls')
tamanho = len(palavra_chave)

palavra_secreta = ["-"] * tamanho #cria um alista com o tamanho da palavra só de "-"
letras_testadas = [] #lista para mostrar as palavras erradas

chances = 5
ganhou = False #variavel de controle para dizer se o jogador ganhou ou perdeu

while chances>0 and ganhou == False:
    print(f"Você tem {chances} tentativa(s)")
    print(*palavra_secreta)

    opc = int(input("1- Testar a letra\n2- Tentar a palavra:\n")) #decisão de passar uma letra ou arriscar a palavra
    
    if opc == 1:
        letra = input("\nDigite a letra para testar: ")
        if letra in letras_testadas: #verifica se existe nas letras testadas
            chances-=1
            print(F"Que pena, repetiu a letra usada. Ainda tem {chances} tentativa(s)")
            print(f"Letras testadas {letras_testadas}") #se existir perde uma chance e mostra a mensagem junto com a lista
        else:
            if letra in palavra_chave: #se existir a letra na palavra chave entra na condicional
                print("Parabéns, acertou a letra!")
                for i in range(tamanho): #loop para percorrer a palavra
                    if letra == palavra_chave[i]: #se a letra for igual a letra daquela posição
                        palavra_secreta[i] = letra #então o "-" da lista da palavra secreta é substituida pela letra
                print(f"Letras testadas {letras_testadas}\n")
                
                if not "-" in palavra_secreta: #aqui faz a verificação se ainda exista alguma letra oculta
                    print("PARABÉNS, VOCÊ GANHOU!") #caso não tenha então o jogador acertou a palavra
                    ganhou = True #e o ganhou passa a ser true e sai do loop
            else: #se não existir ele perde uma chance e a letra vai para a lista de palavras testadas
                chances-=1
                print(F"Que pena, errou a letra. Ainda tem {chances} tentativa(s)")
                letras_testadas.append(letra)
                print(f"Letras testadas {letras_testadas}\n")
    elif opc == 2: #verifica se a palavra digitada é igual a palavra do jogo
        palavra = input("Teste a palavra\n")
        if palavra == palavra_chave:
            ganhou = True
        else:
            chances = 0
    else:
        print("Opção inválida!")


regras.mostra_resultado(ganhou, palavra_chave, chances) #mostra o resultado do jogo