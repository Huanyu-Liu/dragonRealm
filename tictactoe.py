import random

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ""
    while letter != 'X' and letter != 'O':
        letter = input("Do you want to be X or O?\n").upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O','X']

def whoGoesFirst():
    return random.choice(['player', 'computer'])

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

def makeMove(board, move, letter):
    board[move] = letter

def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def getBoardCopy(board):
    copyBoard = []
    for letter in board:
        copyBoard.append(letter)
    return copyBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        move = input("What is your next move\n")
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board,computerLetter):

    if computerLetter == "X":
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1,10):
        copyBoard = getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            makeMove(copyBoard,i,computerLetter)
            if isWinner(copyBoard,computerLetter):
                return i

    for i in range(1,10):
        copyBoard = getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            makeMove(copyBoard,i,playerLetter)
            if isWinner(copyBoard,playerLetter):
                return i

    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    if isSpaceFree(board,5):
        return 5
    move = chooseRandomMoveFromList(board,[2,4,6,8])
    return move

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print("Welcome to Tic Tac Toe!")

while True:
    board = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The " + turn + " will go first")
    isGameFinished = False
    while not isGameFinished:
        if turn == "player":
            drawBoard(board)
            move = getPlayerMove(board)
            board[move] = playerLetter

            if isWinner(board,playerLetter):
                drawBoard(board)
                print("You have beaten the computer. You win!")
                isGameFinished = True
            elif isBoardFull(board):
                drawBoard(board)
                print("You have reached a tie")
                isGameFinished = True

        elif turn == "computer":
            move = getComputerMove(board,computerLetter)
            board[move] = computerLetter

            if isWinner(board,computerLetter):
                drawBoard(board)
                print("The computer has beaten you. You lose!")
                isGameFinished = True
            elif isBoardFull(board):
                drawBoard(board)
                print("You have reached a tie")
                isGameFinished = True

        if not isGameFinished:
            if turn == "player":
                turn = "computer"
            else:
                turn = "player"
        else:
            break
    if not playAgain():
        break


