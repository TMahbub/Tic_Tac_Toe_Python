# Programmed and tested for bugs by Tanjim Mahbub
# Tested for bugs by other people and fixed
from random import randrange
import time
import os

print('''Simple Tic Tac Toe game using basic python.
Choose the number of the box you want to input zero(O)
And the computer will respond with a X
Enjoy

Author: Tanjim Mahbub
''')
def display_board(board):
    print("+"+("-------+" * 3 ))
    print("|"+("       |" * 3 ))
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |" )
    print("|"+("       |" * 3 ))
    print("+"+("-------+" * 3 ))
    print("|"+("       |" * 3 ))
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |" )
    print("|"+("       |" * 3 ))
    print("+"+("-------+" * 3 ))
    print("|"+("       |" * 3 ))
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |" )
    print("|"+("       |" * 3 ))
    print("+"+("-------+" * 3 ))
    return board
    

def enter_move(board):       
    #user_inp = (input("\n\nEnter your move: "))
    while True:
        
        try:
            user_input = int(input("\n\nEnter your move: "))
            if ((user_input >= 1) and (user_input <= 9)):             
                for i in range(3):
                    for j in range(3):                    
                        if ((board[i][j]) == user_input) and (board[i][j] != 'X') and (board[i][j] != 'O'): 
                            board[i][j] = 'O'    
                            #display_board(board)
                            return board  
                print("Wrong input or position already occupied.")
                #user_input = int(input("Enter your move: "))                                    
        except ValueError:
            print("Invalid input, input a number.")


def make_list_of_free_fields(board):
    free = []    
    for i in range(3):
        for j in range(3):
            if (board[i][j] != 'X') and (board[i][j] != 'O'):
                free.append((i,j))
    #print(free)
    return free
    
def draw_move(free):
#    free = make_list_of_free_fields(board)
    #print(free)
    if free:
        move = randrange(len(free))
        i, j = free[move]
        board[i][j],x = 'X',board[i][j]
    print("\nMy move:",x)
    return board

    
    

def victory_for(board):
    
    if board[0][0] == board[0][1] == board[0][2]:
        win = board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        win = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        win = board[2][0] # row done
    
    elif board[0][0] == board[1][0] == board[2][0]:
        win = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        win = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        win = board[0][2] # column done
    
    elif board[0][0] == board[1][1] == board[2][2]:
        win = board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        win = board[1][1] # corners done
        
    else:
        win = 0
    return win
    

def play_game(board):
    display_board(board)
    while True:
        
        enter_move(board)
        display_board(board)
        win = victory_for(board)
        if win != 0:
            break
        free = make_list_of_free_fields(board)
        if len(free) == 0:
            win = 'draw'
            break
        draw_move(free)
        display_board(board)
        win = victory_for(board)
        if win != 0:
            break
        free = make_list_of_free_fields(board)
        if (len(free) == 0):
            win = 'draw'
            break
    if win == 'X':
        print("Computer won !!!")
    elif win == 'O':
        print("You won !!!")
    elif win == 'draw':
        print("Draw !!!")
    

    
while True:
    board = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    play_game(board)
    x = int(input("\nEnter 1 to exit\nor\nEnter 2 to play again: "))
    if x == 1:
        os.system('cls')
        break
    elif x == 2:
        os.system('cls')
    else:
        print("Plase input 1 or 2.")

print("Closing in \n5..")
time.sleep(1)
print("4..")
time.sleep(1)
print("3..")
time.sleep(1)
print("2..")
time.sleep(1)
print("1..")
time.sleep(1)
print("Closing...")
time.sleep(0.5) 
