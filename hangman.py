#!/usr/bin/env python3
#TODO If user got a character right, grant it a free-turn and explain the game

import random, requests

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

def game(tries, name):
    print("It's user", name, "turn")
    matches = [m for m in guessing if m == "_"]
    if not matches: #check if list is empty
        print("Congraz you won with", tries, "tries")

    character = input("Gimme a character: ")
    if character in word:
        print("Alright! the character", character, "is in the word")
        indices = [pos for pos, char in enumerate(word) if char == character]
        for posicion in indices:
            guessing[posicion] = character
    else:
        print("Damn..!", character, "is not in the word")
        
    list_users[user][1] += 1 #+1 to tries of the user which tried
    print(' '.join(guessing))

#everything starts here
qusers = int(input("How many users: "))
lenght = int(input("How many characters should the word have: "))
guessing = [] 
list_users = [] #name = [0], tries = [1]
word = randomword(lenght)
print(word)

for user in range(qusers):
    list = []
    name = input("Your name: ")
    tries = 0
    list.append(name)
    list.append(tries)
    list_users.append(list)

for i in range(lenght):
    guessing.append("_") #generating empty spaces

for _ in range(21+qusers): #to give turns to the other users
    for user in range(len(list_users)): #we use range to iterate between lists
        if list_users[user][1] <= 20:
            game(list_users[user][1], list_users[user][0])
        else:
            #add message to inform about the lost
            pass #not effective , player 1 will lose first, and leave player 2 with 19 turns