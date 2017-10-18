#!/usr/bin/env python3
#TODO show an abecedary with the characters that hasn't been typen yet | stop being case sensitive

import random, requests

class HangmanDone(Exception): pass #to be able to break the loop

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
        raise HangmanDone
    character = input("Gimme a character: ")

    if character in guessing: #if character was already typen, make it to be incorrect if typen again
        print("This letter was already typen, I won't count this try but is not your turn anymore")
    elif character in word:
        print("Alright! the character", character, "is in the word")
        indices = [pos for pos, char in enumerate(word) if char == character]
        for posicion in indices:
            guessing[posicion] = character
            print(' '.join(guessing))
            game(tries, name) #gives back the turn without suming any try
    else:
        print("Damn..!", character, "is not in the word")
        print(' '.join(guessing))
        list_users[user][1] += 1 #+1 to tries of the user which tried  

#everything starts here
qusers = int(input("How many users: "))
lenght = int(input("How many characters should the word have: "))
guessing = [] 
list_users = [] #name = [x][0], tries = [x][1]
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

try:
    for _ in range(21+qusers): #to give turns to the other users
        for user in range(len(list_users)): #we use range to iterate between lists
            if list_users[user][1] <= 20:
                game(list_users[user][1], list_users[user][0])
            else:
                #add message to inform about the lost
                pass
except HangmanDone:
    print("Goodbye, well played")