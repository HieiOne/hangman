#!/usr/bin/env python3
import random, string, requests

lenght = int(input("De cuantas letras quieres la palabra: "))

def randomword(lenght):
    word = ''.join(random.choice(string.ascii_lowercase) for i in range(lenght))
    return word

word = randomword(lenght)
adivinando = []

for i in range(lenght):
    adivinando.append("_")

while True:
    #print(word)
    letra = input("Dime una letra: ")
    if letra in word:
        print("Muy bien la letra", letra, "esta en la palabra")
        indices = [pos for pos, char in enumerate(word) if char == letra]
        for posicion in indices:
            adivinando[posicion] = letra
    else:
        print("La letra", letra, "no esta en la palabra")
    print(' '.join(adivinando))