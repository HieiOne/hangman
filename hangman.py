#!/usr/bin/env python3
#TODO Users

import random, requests

lenght = int(input("How many characters should the word have: "))
guessing = []
tries = 0

for i in range(lenght):
    guessing.append("_") #generating empty spaces

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
    if tries != 20: #death system
        matches = [m for m in guessing if m == "_"]
        if not matches: #check if list is empty
            print("Congraz you won with", tries, "tries")
            break
        character = input("Gimme a character: ")
        if character in word:
            print("Alright! the character", character, "is in the word")
            indices = [pos for pos, char in enumerate(word) if char == character]
            for posicion in indices:
                guessing[posicion] = character
        else:
            print("Damn..!", character, "is not in the word")
        tries += 1
        print(' '.join(guessing))
    else:
        print("You exceeded the 20 tries, you lose..")
        break