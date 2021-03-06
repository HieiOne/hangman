#!/usr/bin/env python3

import random, requests, string

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
        print("Congraz", name, " won with", tries, "tries")
        raise HangmanDone

    print(' | '.join(letters)) #print letters that haven't been used yet
    character = input("Gimme a character: ")

    if character in guessing: #if character was already typen, make it to be incorrect if typen again
        print("This letter was already typen, I won't count this try but is not your turn anymore")
    elif character.upper() in word.upper(): #stop being case sensitive
        print("Alright! the character", character.lower(), "is in the word")
        letters.remove(character.upper())
        indices = [pos for pos, char in enumerate(word) if char == character.lower()]
        for posicion in indices:
            guessing[posicion] = character.lower()
        print(' '.join(guessing))
        game(tries, name) #gives back the turn without suming any try
    else:
        print("Damn..!", character, "is not in the word")
        letters.remove(character.upper())
        print(' '.join(guessing))
        list_users[user][1] += 1 #+1 to tries of the user which tried  

#everything starts here
qusers = int(input("How many users: "))
lenght = int(input("How many characters should the word have: "))
guessing = [] 
list_users = [] #name = [x][0], tries = [x][1]
letters = list(string.ascii_uppercase) # this is a dictionary even if it doesn't look like one
word = randomword(lenght)
#print(word) #cheats on

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
        for user in range(len(list_users)): #we use range to iterate between lists (enumerate)
            if list_users[user][1] <= 20:
                game(list_users[user][1], list_users[user][0])
            else:
                #add message to inform about the lost
                pass
except HangmanDone:
    print("Goodbye, well played")