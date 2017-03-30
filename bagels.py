import random

def getSecretNum(numOfDigit):
    numberList = list(range(10))
    random.shuffle(numberList)
    secretNum = ""
    for i in range(numOfDigit):
        secretNum += str(numberList[i])
    return secretNum

def getClues(guess, secretNum):
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append("Fermi")
        elif guess[i] in secretNum:
            clue.append("Pico")
    if len(clue) == 0:
        clue.append("Bagel")
    if guess == secretNum:
        return "You got it"
    return " ".join(clue)

def isOnlyDigit(num):
    if num == "":
        return False
    for i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False
    return True

def playAgain():
    print("Do you want to play again? (Yes or no)")
    return input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print("I have thought up a number. You have %s guesses to get it." %(MAXGUESS))
    numberOfGuess = 1
    while numberOfGuess <= MAXGUESS:
        guess = ""
        while len(guess) != NUMDIGITS or not isOnlyDigit(guess):
            guess = input("Guess #%s:\n" %(numberOfGuess))
        clue = getClues(guess,secretNum)
        numberOfGuess += 1
        print(clue)
        if guess == secretNum:
            break
    if numberOfGuess > MAXGUESS:
        print("You have run out of guesses. You lose!")
    if not playAgain():
        break
