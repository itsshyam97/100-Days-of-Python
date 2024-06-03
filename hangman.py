import random
import hangmanModule
import os

print(hangmanModule.logo)

words = hangmanModule.word_list
count = 1
hangList = hangmanModule.stages
gameOver = False
finalWord = ''

word = random.choice(words)

wordList = []
for i in word:
    wordList += '_'

for z in wordList:
    print(z, end = ' ')

def hangman(count,gameOver,finalWord):

    userInput = input("\nGuess a letter : ").lower()

    os.system('cls')
    
    for i in range(len(word)):
        if word[i] == userInput:
            wordList[i] = userInput
    for i in wordList:
        print(i, end = ' ')

    print(f"{hangList[-count]}")

    if userInput not in wordList:

        # print(f"{hangList[-count]}")
         
        if count >= len(hangList):
            gameOver = True
            print("\nGame Over.")
            exit()
        
        count += 1

    if '_' not in wordList:
        for i in wordList:
            finalWord += i
        print("\nYou won!!!")
        exit()
        
    while not gameOver:
        hangman(count,gameOver,finalWord)
    
hangman(count,gameOver,finalWord)