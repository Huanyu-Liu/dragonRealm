import random
HANGMANPICS = ['''
    +-------+
    |       |
            |
            |
            |
            |
================''','''
    +-------+
    |       |
    O       |
            |
            |
            |
================''','''
    +-------+
    |       |
    O       |
    |       |
            |
            |
================''','''
    +-------+
    |       |
    O       |
   /|       |
            |
            |
================''','''
    +-------+
    |       |
    O       |
   /|\      |
            |
            |
================''','''
    +-------+
    |       |
    O       |
   /|\      |
   /        |
            |
================''','''
    +-------+
    |       |
    O       |
   /|\      |
   / \      |
            |
================''']

words = {"fruit":'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         "color":'red orange yellow green blue indigo violet white black brown'.split(),
         "shape":'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         "animal":'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    return [random.choice(wordDict[wordKey]),wordKey]

def displayBoard(HANGMANPICS, missedWords, correctWords, secretWord):
    print(HANGMANPICS[len(missedWords)])
    print()
    print("Missed Letters: ",end="")
    for letter in missedWords:
        print(letter,end=" ")
    print()
    wordLength = len(secretWord)
    blank = '_' * wordLength
    for i in range(0,wordLength):
        if secretWord[i] in correctWords:
            blank = blank[:i] + secretWord[i] + blank[i+1:]
    for letter in blank:
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    while True:
        guess = input("Guess a letter\n")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Please try again")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER")
        else:
            return guess

def playAgain():
    print("Do you want to play again? (Yes or no)")
    playAgain = input()
    return playAgain.lower().startswith('y')


print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord, wordKey = getRandomWord(words)
gameIsDone = False
while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    print("The secret word is in the set: \"" + wordKey + "\"")
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        foundAllLetters = True
        correctLetters = correctLetters + guess
        for letter in secretWord:
            if letter not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is \"" + secretWord + "\"! You have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print("You have missed out of guesses.\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guessed, the word was \"" + secretWord + "\"!")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            secretWord, wordKey = getRandomWord(words)
            gameIsDone = False
        else:
            break

