"""PROBLEMA: 1131 - Grenais"""

#váriaveis necessárias para a resolução
gols_inter = 0
gols_gremio = 0
empate = 0
inter = 0
gremio = 0
total = 0

#while true não necessita de uma variavél de inicialização
while True:
    # 1- começa recebendo o placar do jogo(interXgremio respectivamente)
    # 2- e já verifica qm foi o ganhador ou se foi empate, e assim já começa a contar quem ganhou mais
    # 3- em senquancia já faz o total de grenais
    gols_inter, gols_gremio = map(int,(input().split(" ")))
    if gols_inter > gols_gremio:
        inter+=1
    elif gols_inter < gols_gremio:
        gremio+=1
    else:
        empate+=1
    total+=1
    
    # 1- verifica se teve outro grenal
    # 2- se tiver ele nvolta para o loop
    # 3- caso não tenha ele printa os resultados e verifica quem ganhou mais ou se foi empate da quantidade de vitórias
    # 4- e já mostra o resultado final do ganhador ou empate e fecha o loop com o break
    resp = int(input("Novo grenal (1-sim 2-nao)\n"))
    if resp == 2:
        print("%d grenais"%(total))
        print("Inter:%d"%(inter))
        print("Gremio:%d"%(gremio))
        print("Empates:%d"%(empate))
        
        if inter>gremio:
            print("Inter venceu mais")
            break
        elif inter<gremio:
            print("Gremio venceu mais")
            break
        else:
            print("Nao houve vencedor")
            break