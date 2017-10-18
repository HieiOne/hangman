#!/usr/bin/env python3
#TODO Users and Tries + Death system(maximum tries)

import random, requests

lenght = int(input("De cuantas letras quieres la palabra: "))
adivinando = []

for i in range(lenght):
    adivinando.append("_") #generating empty spaces

def randomword(lenght):
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    dictionary = requests.get(word_site)
    #.text formats the words, and .splitlines() let's me grab a word
    words = dictionary.text.splitlines()
    accepted_words = []
    for every_word in words:
        if len(every_word) == lenght:
            accepted_words.append(every_word)
    word = random.choice(accepted_words)
    return word
word = randomword(lenght)

while True:
    matches = [m for m in adivinando if m == "_"]
    if not matches: #check if list is empty
        print("Congraz you won")
        break
    letra = input("Dime una letra: ")
    if letra in word:
        print("Muy bien la letra", letra, "esta en la palabra")
        indices = [pos for pos, char in enumerate(word) if char == letra]
        for posicion in indices:
            adivinando[posicion] = letra
    else:
        print("La letra", letra, "no esta en la palabra")
    print(' '.join(adivinando))
