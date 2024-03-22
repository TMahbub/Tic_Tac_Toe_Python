# Programmed and tested for bugs by Tanjim Mahbub
from random import randrange

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
    #win = None
    
    if board[0][0] == board[0][1] == board[0][2]:
        win = board[0][0]
            #break
    elif board[1][0] == board[1][1] == board[1][2]:
        win = board[1][0]
    #        break
    elif board[2][0] == board[2][1] == board[2][2]:
        win = board[2][0] # row done
    #        break
    elif board[0][0] == board[1][0] == board[2][0]:
        win = board[0][0]
    #        break
    elif board[0][1] == board[1][1] == board[2][1]:
        win = board[0][1]
    #        break
    elif board[0][2] == board[1][2] == board[2][2]:
        win = board[0][2] # column done
    #        break   
    elif board[0][0] == board[1][1] == board[2][2]:
        win = board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        win = board[1][1]
        
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
        #print("Free box =",free, "\nlength =", len(free))
        if len(free) == 0:
            win = 'draw'
            print("Draw")
            break
        draw_move(free)
        display_board(board)
        win = victory_for(board)
        if win != 0:
            break
        free = make_list_of_free_fields(board)
        #print("free box =",free, "\nlength =", len(free))
        if (len(free) == 0):
            win = 'draw'
            break
        #else:
        #    win = victory_for(board)
        #win = victory_for(board)
        #if win != 0:
        #    break
    
    if win == 'X':
        print("Computer won !!!")
    #        break
    elif win == 'O':
        print("You won !!!")
    #        break
    elif win == 'draw':
        print("Draw !!!")
    #        break
        #else:
        #    continue
    

    
board = [ [1, 2, 3], [4, 'X', 6], [7, 8, 9] ]
play_game(board)