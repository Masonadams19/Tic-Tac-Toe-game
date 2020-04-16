#! /masonadams/env python3

import os

board = list("1 | 2 | 3 \n--------- \n4 | 5 | 6 \n--------- \n7 | 8 | 9")
#"1" = 0
#"2" = 4
#"3" = 8
#"4" = 22
#"5" = 26
#"6" = 30
#"7" = 44
#"8" = 48
#"9" = 52
boards = "".join(board)
print(boards) #shows starting gamwboard to players

#converts the string number positions from the game board to integer positions in the
#list for the function to execute
def plcconvert(boardplc):
    plc = 0
    if boardplc == "1":
        return 0
    elif boardplc == "2":
        return 4
    elif boardplc == "3":
        return 8
    elif boardplc == "4":
        return 22
    elif boardplc == "5":
        return 26
    elif boardplc == "6":
         return 30
    elif boardplc == "7":
        return 44
    elif boardplc == "8":
        return 48
    elif boardplc == "9":
        return 52

def tic_toe(sym,plc): 
    global board
     # plc = place, or where the symbol will be put
     # sym = the symbol the user wants to enter
     #the following correlates integrer position in printed board to string position
     
     #"1" = 0
     #"2" = 4
     #"3" = 8
     #"4" = 22
     #"5" = 26
     #"6" = 30
     #"7" = 44
     #"8" = 48
     #"9" = 52
     
    if sym == plc:
        # resets board and prints it if both variables are equal
        board = "1 | 2 | 3 \n--------- \n4 | 5 | 6 \n--------- \n7 | 8 | 9"
        print(board)
    else:
        space = ""
        #creates a list of the string board
        boardlst = list(board)
        # changes the chosen position to the chosen symbol
        boardlst[plc] = sym
        # creates a string of the board in the correct format
        board = space.join(boardlst)
        # prints the board with the symbol!
        print(board)


#actual function that runs
        
winner = False
turns = 0
while winner != True: #loops until winner is declared
    print("\nEnter a symbol to be used to mark your positions")
    sym = input("symbol:") #asks for a symbol for the player
    if sym.islower() and sym.isalpha(): #checks if the character is a letter, and capitalizes if it is
        sym = sym.capitalize()
    print("Enter a position on the board from 1-9")
    boardplc = input("position:") #asks for a position from 1-9
    plc = plcconvert(boardplc) #converts integer place to list position
    
    try: #bypasses error if user integrs string instead of integer
        print("\n ")
        tic_toe(sym,plc)
        #checks for winning sequences
        if board[0] == board[4] and board[4] == board[8]:
            print("\nCongragulations " + sym + ", you have won!!!")
            cont = input("Continue playng? (y/n):")
            if cont == "y": #asks if the player wnats to continue, and resets the board if true
                board = "1 | 2 | 3 \n--------- \n4 | 5 | 6 \n--------- \n7 | 8 | 9"
                print("\n\n\n" + "New Game\n" + board)
            else:
                winner = True
                print("Thanks for playing!")
        elif board[22] == board[26] and board[26] == board[30]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif board[44] == board[48] and board[48] == board[52]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif board[0] == board[22] and board[22] == board[44]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif board[4] == board[26] and board[26] == board[48]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif board[8] == board[30] and board[30] == board[52]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif board[0] == board[26] and board[26] == board[52]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif board[8] == board[26] and board[26] == board[44]:
            winner = True
            print("\nCongragulations " + sym + ", you have won!!!")
        elif turns == 8: #checks for a draw
            winner = True
            print("\nScratch! No winner")
        else:
            turns = turns + 1
            continue
    except: #if the word "nine" is entered instead of "9", will ask for the integer
        print("Enter a integer, not word, from 1-9")
        boardplc = input("position:")
        continue
        
        




