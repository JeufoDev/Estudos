"""PROBLEMA: 1142 - PUM"""
numero = int(input())
contador = 1

for i in range(numero):
    for e in range(3):
        print(contador, end=" ")
        contador+=1
    contador+=1
    print("PUM")