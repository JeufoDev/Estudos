"""PROBLEMA: 1848 - Corvo Contador"""
"""Regras do corvo:"""
#são 3 olhos representados por -(fechado) *(aberto)
#os olhos são representados em binário(fazer conversão)
#sempre que ele gritar é exibido a soma da sequencia dos olhos
#ele só pode gritar 3 vezes

#fiz com listas e com dicionarios, no site ficou mais rapido assim
olhos = {"---":0,
         "--*":1,
         "-*-":2,
         "-**":3,
         "*--":4,
         "*-*":5,
         "**-":6,
         "***":7}

#variáveis de controle
soma = 0
gritos = 3
while gritos>0: #enquanto os gritos > 0 ele vai executar
    resposta = input() #recebe da entrada padrão se é sequencia de olhos ou grito
    if resposta in olhos: #se existir em olhos ele soma os valores das chaves passadas
        soma += olhos[resposta] #somatorio
    elif resposta == "caw caw": #se a resposta for o grito ele printa e subtrai um grito e reseta pra 0 a soma
        print(soma)
        soma = 0
        gritos-=1
    #aqui poderia utilizar um else para tratamento de erro
    #mas não foi necessário para o site