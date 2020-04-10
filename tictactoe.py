import random
#player 1 is X
#player 2 is O
player = random.randrange(1,3)
print(player)
turn = 1
board = [' ',' ',' ',' ',' ',' ',' ',' ',' '  ]
gameOver = False

def printBoard():
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')

def instructionBoard():
    board = ['0','1','2','3','4','5','6','7','8'  ]
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')

def switchPlayer():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

def winCheck(player):
    global board
    letter = ''
    if player == 1:
        letter = 'X'
    else:
        letter = 'O'
    return ((letter == board[0] and board[0] == board[1] and board[1] == board[2]) or 
    (letter == board[3] and board[3] == board[4] and board[4] == board[5]) or 
    (letter == board[6] and board[6] == board[7] and board[7] == board[8]) or 
    (letter == board[0] and board[0] == board[3] and board[3] == board[6]) or 
    (letter == board[7] and board[7] == board[1] and board[1] == board[4]) or 
    (letter == board[8] and board[8] == board[5] and board[5] == board[2]) or 
    (letter == board[0] and board[0] == board[4] and board[4] == board[8]) or 
    (letter == board[6] and board[6] == board[4] and board[4] == board[2]))
    
def checkTie():
    global board
    global gameOver
    if ' ' not in board:
        print("The game is a tie")
        gameOver = True
def playerMove():
    global player
    global board
    print("Hello Player %s, what move would you like to make? (0-8)"% player)
    moved = False
    while moved == False:
        move = input()
        move = int(move)
        if move > 8:
            print("That is not a valid move, please try again.")
        elif board[move] != ' ':
            print("That space is already occupied, please input a valid move.")
        elif board[move] == ' ':
            if player == 1:
                board[move] = 'X'
            elif player == 2:
                board[move] = 'O'
            moved = True

    

print("Welcome to Tic Tac Toe, Player %s it is your turn"% player)

instructionBoard()
while gameOver == False:
    playerMove()
    if winCheck(player) == True:
        gameOver = True
        print("Congratulations Player %s"% player)
        break
    checkTie()
    switchPlayer()
    printBoard()
