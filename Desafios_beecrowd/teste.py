"""PROBLEMA: 1145 - Sequência Lógica 2"""

x,y = map(int,input().split())
contador = 1

while contador<=y:
    for e in range(1,x):
        print (contador, end=' ')
        contador+=1
    print(contador)
    contador+=1