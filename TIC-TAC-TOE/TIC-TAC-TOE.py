players=['','X','O']
Board=[' ']*10
score=['',0,0]


from IPython.display import clear_output

def display_board(board):
    
    print(f'   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print(f'---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print(f'---|---|---')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print(f'   |   |')


def player_input():
    play1=' '
    while play1 not in  ('X','O'):
        play1=input('Player 1 : Choose either \'X\' or \'O\' : ').upper()
    if play1=='X':
        play2='O'
    else:
        play2='X'
    return (play1,play2)



def place_marker(board, marker, position):
    board[position]=marker



def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[4] ==  board[5] ==  board[6] == mark) or 
    (board[7] ==  board[8] ==  board[9] == mark) or
    (board[7] ==  board[4] ==  board[1] == mark) or 
    (board[8] ==  board[5] ==  board[2] == mark) or
    (board[9] ==  board[6] ==  board[3] == mark) or
    (board[7] ==  board[5] ==  board[3] == mark) or
    (board[9] ==  board[5] ==  board[1] == mark))



import random

def choose_first():
    return random.choice((-1,1))



def space_check(board, position):
    return board[position]==' '



def full_board_check(board):
    return not ' ' in board[1:]


def player_choice(board,player):
    pos = 0
    while pos not in range(1,11) or not space_check(board,pos):
        try:
            pos = int(input(f'Player{player} Enter the position : '))
        except:
            print('Sorry try again')
    return pos


def replay():
    return input('Do you want to play again (Yes/No) : ').lower()=='yes'



def gridfor():
    print(f'   |   |')
    print(f' 7 | 8 | 9')
    print(f'---|---|---')
    print(f' 4 | 5 | 6')
    print(f'---|---|---')
    print(f' 1 | 2 | 3')
    print(f'   |   |')


def scorepr():
    print (f'Player 1 : {score[1]}')
    print (f'Player 2 : {score[2]}')
    
    

print('Welcome to Tic Tac Toe!')
print ('\ngrid format : ')
gridfor()
x=1
while True:
    print ('\nSCORE BOARD :')
    scorepr()
    ind = choose_first()
    player = players[ind]
    print(f'This is round {x}, Player {player} will go first!')
    ongoing = True
    input('Hit Enter to continue')
    while ongoing:
        display_board(Board)
        print('\n')
        gridfor()
        position = player_choice(Board,player)
        place_marker(Board,player,position)
        
        if win_check(Board, player):
            display_board(Board)
            print('Congratulations! Player '+player+' wins!')
            score[ind]+=1 
            ongoing = False
        else:
            if full_board_check(Board):
                display_board(Board)
                print('The game is a draw!')
                break
            else:
                ind *= -1
                player = players[ind]
                clear_output()
                
    Board = [' '] * 10
    x+=1
    
    if not replay():
        break
print('\nFINAL SCORE :')
scorepr()
score=['',0,0]

