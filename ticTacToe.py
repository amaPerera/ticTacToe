# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:54:31 2019

@author: Ama

Tic Tac Toe Game in Python
"""
#creating the board
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

#printing th board 
def printBoard(board):
    print('-------------')
    for i in range(3):
        print('|   |   |   |')
        print('| ' + board[i*3+1] + ' | ' + board[i*3+2] + ' | ' + board[i*3+3] + ' |')
        print('|   |   |   |')
        print('-------------')
        
#b is board l is letter
#checking whether there is a winner according to the current board
#we need to check every single line is populated with the same letter
def isWinner(b, l):
    return ((b[7] == l and b[8] == l and b[9] == l) or # across the top
    (b[4] == l and b[5] == l and b[6] == l) or # across the middle
    (b[1] == l and b[2] == l and b[3] == l) or # across the bottom
    (b[7] == l and b[4] == l and b[1] == l) or # down the left side
    (b[8] == l and b[5] == l and b[2] == l) or # down the middle
    (b[9] == l and b[6] == l and b[3] == l) or # down the right side
    (b[7] == l and b[5] == l and b[3] == l) or # diagonal
    (b[9] == l and b[5] == l and b[1] == l)) # diagonal

def playerMove():
    #we define this variable as we dont want to run the game unless the user havent give a valid answer 
    run = True
    while run:
        move = input('Please enter a position to place \'x\' from 1 to 9: ')
        #now we go to a try except statement just to make sure that the user giving us a number as we dont want the program to crash, so we would throug an error
        #and we want to catch that error and move forward with the program ask user again and again to write another one till the user gives a valid input
        try:
            move = int(move) # if they give us a string like 'hi' this will crash the program and go to our except statement
            #Check the move is in the range of 1 to 9
            if move > 0 and move < 10:
                #now we have a valid move and need to check whether the position is already aoccupied
                if spaceIsFree(move):
                    #now we have got a valid answer so we dont need to run the input again and again so we change run in to False
                    run = False
                    #now we inser the x into the board
                    insertLetter('X',move)
                #If these are not go well then we need to tell the user what went wrong
                else:
                    print('OOPS! That space is occupied! Please enter another position.')
            else:
                print('The position is not valid, Please enter valid position between 1 and 9.')
        except:
            print('Please type a number!')
            
#Now comes the AI stuff.. :)
def compMove():
    pass

#selecting a randome position from the given list of positions
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

#It is easier to put this in a function as we dont want to repeat the code :)
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print ('Let\'s play Tic Tac Toe!!!' )
    printBoard(board)
    
    while not(isBoardFull (board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, Computer has won!!!')
            break
        
        if not(isWinner(board,'X')):
            move = compMove()
            if move == 0: # the board is full so the computer couldn't move
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer place \'O\' in positon', move)
                printBoard()
        else:
            print('You won! Good Job!! :)')
            break
    
    if isBoardFull (board):
        print('Tie Game!')
        
        

main()
print('#')
print(board.count(' '))