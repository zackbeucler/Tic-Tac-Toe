# coding=utf-8
import random


def showGameRules():
    # This function prints out the rules at the beginning of the game
    print("Tic Tac Toe!\n\n")
    """
    print("RULES...................\n\n")
    print("1.  Two players select spaces on the 3×3 grid. The two players alternate when choosing spaces. (First turn should be selected randomly.)\n\n")
    print("2. If a player gets three in a row horizontally, vertically, or diagonally in any fashion, this player wins the game.\n\n")
    print("3. If the game continues until all the spaces are selected and neither player has three in a row, then the match is a draw/push.\n\n")
    print("To select a space, type one of the corresponding indices:\n\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n\n")
    """


def askPlayerName(i):
    # This function asks for a player name and returns it
    return input("Player "+str(i)+" enter your name: ")


def firstMove(player0, player1):
    # This function takes the two players as parameters and chooses and returns the first player at random
    if(random.randint(0, 1) == 0):
        return player0
    else:
        return player1


def playerPickSymbol(first):
    # This function takes the first player as a parameter nd then returns the symbol they choose
    return input("\n"+first+", you go first! Type 'X' or 'O' to choose your symbol:  ")


def answer():
    answer = playerPickSymbol("player")
    return answer


def placePiece(player, i, symbols, board):
    # This function takes the player, their symbol index, the list of symbols, and the board list as parameters
    # The user chooses their space, and the function adds the selection to the board list and returns the board list
    taken = True
    while(taken):
        selection = eval(input("\n"+player+", make your selection: \n"))
        if(board[selection-1] == " "):
            taken = False
        else:
            print("\nThis space is taken. Try again: ")

    board[selection-1] = symbols[i]
    return board


def outputGameBoard(board):
    # This function takes the board list as a parameter and prints out the current state of the game board
    print("\n", board[0], "|", board[1], "|", board[2], "\n----------\n", board[3], "|",
          board[4], "|", board[5], "\n----------\n", board[6], "|", board[7], "|", board[8]+"\n")


def checkWinner(board, symbols, player0, player1):
    # This function takes the board, symbols list, and both players as parameters, checks the game board to see if there is a winner,
    # and outputs and returns the winner if there is one
    if(board[1] != " " and board[1] == board[0]):
        if(board[2] == board[1]):
            if(board[1] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[5] != " " and board[5] == board[2]):
        if(board[8] == board[5]):
            if(board[5] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[4] != " " and board[4] == board[1]):
        print("True")
        if(board[7] == board[4]):
            if(board[4] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[4] != " " and board[4] == board[3]):
        if(board[5] == board[4]):
            if(board[4] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[7] != " " and board[7] == board[6]):
        if(board[8] == board[7]):
            if(board[7] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[3] != " " and board[3] == board[0]):
        if(board[3] == board[6]):
            if(board[0] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[4] != " " and board[4] == board[0]):
        if(board[8] == board[4]):
            if(board[4] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
            return True

    elif(board[4] != " " and board[4] == board[2]):
        if(board[6] == board[4]):
            if(board[4] == symbols[0]):
                print(player0, "has won!")
            else:
                print(player1, "has won!")
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
        print("The board is full so the game ends in a tie.")
        return True
    return False


def playAgain():
    # This function asks the user if they want to play again and returns their answer asn a boolean
    again = input("\nType 'p' to play again or type 'q' to quit: ")
    if(again.lower() == 'p'):
        return True
    return False


def play_tic_tac_toe():
    # main function from which all other functions are called
    # runs through the tic tac toe game in proper order
    again = True

    while(again):
        showGameRules()

        player0 = askPlayerName(0)
        print('\n')
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

            turn = turn + 1
            i = i + 1

            if(checkWinner(board, symbols, player0, player1)):
                winner = False
            if(fullBoard(board)):
                full = False

        if(playAgain() is not True):
            again = False

    def main():
        play_tic_tac_toe()  # starts a game of tic tac toe


def main():
        play_tic_tac_toe()  # starts a game of tic tac toe

if __name__ == "__main__":
    main()

    if __name__ == "__main__":
        main()

