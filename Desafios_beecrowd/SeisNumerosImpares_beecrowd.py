"""Problema: 1070 - Seis Números Ímpares"""

numero = int(input())
contador = 0

while contador <6:
    if numero%2 !=0:
        print(numero)
        numero+=1
        contador +=1
    numero+=1