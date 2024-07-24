def display(board):
    print(board[7] + '|' + board[8] + '|' +  board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' +  board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' +  board[3])


mylist = [' '] * 10
#display(mylist)

def player_input():
    choice = 'wrong'

    while choice != 'X' and choice != 'O':
        choice = input("Please choose between 'x' or 'o': ").upper()
    
    return choice
#player_input()

def place_marker(board, marker, position):
    board[position] = marker
    
place_marker(mylist,'$',8)
display(mylist)