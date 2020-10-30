import random
playAgain = True
while(playAgain):
    print("Tic Tac Toe!\n\n")
    print("RULES...................\n\n")
    print("1.  Two players select spaces on the 3×3 grid. The two players alternate when choosing spaces. (First turn should be selected randomly.)\n\n2.  If a player gets three in a row horizontally, vertically, or diagonally in any fashion, this player wins the game.\n\n3.  If the game continues until all the spaces are selected and neither player has three in a row, then the match is a draw/push.\n\n")
    print("To select a space, type one of the corresponding indices:\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n\n")

    PZ = True
    while(PZ):
        player0 = input("Player 0, enter your name: ")
        c = input("\nPress enter to confirm your name is "+player0+": ")
        if(c == ""):
            PZ = False

    PW = True
    while(PW):
        player1 = input("\nPlayer 1, enter your name: ")
        c = input("\nPress enter to confirm your name is "+player1+": ")
        if(c == ""):
            PW = False

    i = 2
    if(random.randint(0,1) == 0):
        first = player0
    else:
        first = player1
        i = 3

    s = True
    while(s):
        symbol = input("\n"+first+", you go first! Type 'X' or 'O' to choose your symbol:  ")
        c = input("\nPress enter to confirm your symbol is "+symbol+": ")
        if(c == ""):
            s = False
    if(symbol.lower() == 'x'):
        symbol0 = 'X'
        symbol1 = 'O'
    else:
        symbol1 = 'X'
        symbol0 = 'O'

    board = [" "," "," "," "," "," "," "," "," "]
    full = True
    winner = True
    turn = 0
    while(winner and turn<9):
        confirm = True
        while(confirm):
            selection=0
            while(True):
                if(i%2==0):
                    selection = eval(input("\n"+player0+", make your selection: "))
                    current = player0
                else:
                    selection = eval(input("\n"+player1+", make your selection: "))
                    current = player1
                if(1<=selection<=9):
                    break
                else:
                    print("Not a valid space")
            conf =""
            if(board[selection-1]!=" "):
                print("\nNot an open space. Pick again.")
            else:
                conf = input("\nPress enter to confirm that you selected space "+str(selection)+": ")
            if(conf == ""):
                confirm = False
                if(current == player0):
                    board[selection-1] = symbol0
                else:
                    board[selection-1] = symbol1
        print("\n",board[0],"|",board[1],"|",board[2],"\n----------\n",board[3],"|",board[4],"|",board[5],"\n----------\n",board[6],"|",board[7],"|",board[8])
        count = 0
        if(board[4]!=" " and board[4] == board[2]):
            if(board[6] == board[4]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        elif(board[1]!=" " and board[1] == board[0]):
            if(board[2] == board[1]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        elif(board[4]!=" " and board[4] == board[3]):
            if(board[5] == board[4]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        elif(board[7]!=" " and board[7] == board[6]):
            if(board[8] == board[7]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        elif(board[3]!=" " and board[3] == board[0]):
            if(board[3] == board[6]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        elif(board[4]!=" " and board[4] == board[1]):
            if(board[7] == board[4]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        elif(board[5]!=" " and board[5] == board[2]):
            if(board[8] == board[5]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        if(board[4]!=" " and board[4] == board[0]):
            if(board[8] == board[4]):
                if(board[0] == symbol0):
                    print(player0,"has won!")
                else:
                    print(player1,"has won!")
                winner = False
        turn = turn + 1
        i = i + 1
        
    again = input("Press enter to play again or type 'q' to quit: ")
    if(again!=""):
        playAgain = False
        
        

