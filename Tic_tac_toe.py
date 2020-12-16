# coding=utf-8
import random
from game_log import log

def showGameRules():
    # This function prints out the rules at the beginning of the game
    print("Tic Tac Toe!\n\n")
    print("RULES...................\n\n")
    print("1.  Two players select spaces on the 3×3 grid. The two players alternate when choosing spaces. (First turn should be selected randomly.)\n\n")
    print("2. If a player gets three in a row horizontally, vertically, or diagonally in any fashion, this player wins the game.\n\n")
    print("3. If the game continues until all the spaces are selected and neither player has three in a row, then the match is a draw/push.\n\n")
    print("To select a space, type one of the corresponding indices:\n\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n")

def askPlayerName(i):
    # This function asks for a player name and returns it
    # only error is if the player doesent enter a name at all
    playerName = input("\nPlayer "+str(i)+" enter your name: ")
    while playerName == "":
        print("Invalid name entered")
        playerName = input("Player "+str(i)+" enter your name: ")
    return playerName


def firstMove(player0, player1):
    # This function takes the two players as parameters and chooses and returns the first player at random
    if(random.randint(0, 1) == 0):
        return player0
    else:
        return player1


def playerPickSymbol(first):
    # This function takes the first player as a parameter nd then returns the symbol they choose
    playerSymbol = input("\n"+first+", you go first! Type 'X' or 'O' to choose your symbol:  ")

    # while the player hasnt entered any of the desired symbols
    while playerSymbol != "X" and playerSymbol != "x" and playerSymbol != "O" and playerSymbol != "o":
        print("\nInvalid Symbol entered. Please type 'X' or 'O':" )
        playerSymbol = input("\n"+first+", you go first! Type 'X' or 'O' to choose your symbol:  ")  # ask them again until they enter a correct symbol

    return playerSymbol


def answer():
    answer = playerPickSymbol("player")
    return answer


def placePiece(player, i, symbols, board):
    # This function takes the player, their symbol index, the list of symbols, and the board list as parameters
    # The user chooses their space, and the function adds the selection to the board list and returns the board list

    #error handling
    valid = False
    
    while(not valid):
        taken = True
        try:
            selection = int(input("\nPlease enter the index of the space you would like to select: "))
            if(board[selection-1] != " "):
                print("\nSorry! This space is already taken. Please take another look at the board and pick a different space.")
                outputGameBoard(board)
            else:
                board[selection-1] = symbols[i]
                taken = False
        except(ValueError, IndexError):
            print("\nSorry! The integer you have entered is not valid or the space is already taken. Please"+ 
            " make sure you are entering an integer between 1 and 9.")
            outputGameBoard(board)
        
        if(taken == False):
            valid = True
        log.info("selection: "+str(selection))

    return board

def outputGameBoard(board):
    # This function takes the board list as a parameter and prints out the current state of the game board
    print("\n", board[0], "|", board[1], "|", board[2], "\n----------\n", board[3], "|",
          board[4], "|", board[5], "\n----------\n", board[6], "|", board[7], "|", board[8])


def checkWinner(board, symbols, player0, player1):
    # This function takes the board, symbols list, and both players as parameters, checks the game board to see if there is a winner,
    # and outputs and returns the winner if there is one
    if(board[1] != " " and board[1] == board[0]):
        if(board[2] == board[1]):
            if(board[1] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[5] != " " and board[5] == board[2]):
        if(board[8] == board[5]):
            if(board[5] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[4] != " " and board[4] == board[1]):
        print("True")
        if(board[7] == board[4]):
            if(board[4] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[4] != " " and board[4] == board[3]):
        if(board[5] == board[4]):
            if(board[4] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[7] != " " and board[7] == board[6]):
        if(board[8] == board[7]):
            if(board[7] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[3] != " " and board[3] == board[0]):
        if(board[3] == board[6]):
            if(board[0] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[4] != " " and board[4] == board[0]):
        if(board[8] == board[4]):
            if(board[4] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    if(board[4] != " " and board[4] == board[2]):
        if(board[6] == board[4]):
            if(board[4] == symbols[0]):
                print("\n"+player0, "has won!")
            else:
                print("\n"+player1, "has won!")
            return True

    return False


def fullBoard(board):
    # This function takes the game board list as a parameter and returns a boolean for if the board is full or not
    count = 0
    for space in board:
        if(space == " "):
            break
        else:
            count += 1
    if(count == 9):
        print("\nThe board is full so the game ends in a tie.")
        return True
    return False


def playAgain():
    # This function asks the user if they want to play again and returns their answer asn a boolean
    valid = True  # error handling
    validInputs = ['p', 'q']

    while(valid):  # handles error --> invalid input
        again = input("\nType 'p' to play again or type 'q' to quit: ")
        if(again.lower() not in validInputs):
            print("\n")
        else:
            if(again.lower() == 'p'):
                return True
            else:
                print("\nThanks for playing!")
                valid = False
    return False


def play_tic_tac_toe():
    # main function from which all other functions are called
    # runs through the tic tac toe game in proper order
    again = True

    while(again):
        showGameRules()

        player0 = askPlayerName(0)
        player1 = askPlayerName(1)

        i = 3
        first = player1
        if(player0 == firstMove(player0, player1)):
            i = 2
            first = player0

        firstSymbol = playerPickSymbol(first).lower()
        symbols = [-1, -1]
        if(first == player0):
            if(firstSymbol == 'x'):
                symbols[0] = 'X'
                symbols[1] = 'O'
            else:
                symbols[1] = 'X'
                symbols[0] = 'O'
        else:
            if(firstSymbol == 'x'):
                symbols[1] = 'X'
                symbols[0] = 'O'
            else:
                symbols[0] = 'X'
                symbols[1] = 'O'

        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        full = True
        winner = True
        turn = 0
        while(winner and turn < 9):
            if(i % 2 == 0):
                board = placePiece(player0, 0, symbols, board)
                current = player0
            else:
                board = placePiece(player1, 1, symbols, board)
                current = player1

            outputGameBoard(board)
            log.info("current player: "+current)

            turn = turn + 1
            i = i + 1

            if(checkWinner(board, symbols, player0, player1)):
                winner = False
                turn = 9
            if(fullBoard(board)):
                full = False
                winner = False
                turn = 9

            log.info("winner? "+str(not winner))
            log.info("full? "+str(not full))

        if(playAgain() is not True):
            again = False
            break


def main():
        play_tic_tac_toe()  # starts a game of tic tac toe

if __name__ == "__main__":
    main()

