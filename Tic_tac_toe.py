import random

def display_board(board):
    print(board[7] + '|' + board[8] + '|' +  board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' +  board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' +  board[3])

mylist = [' '] * 10
#display(mylist)
def place_marker(board, marker, position):
    board[position] = marker

def player_input():
    marker = 'wrong'

    while marker not in ['X', 'O']:
      marker = input("Please choose between 'x' or 'o': ").upper()
    
    if marker == 'X':
      return('X', 'O')
    else:
      return('O', 'X')

def win_check(board, mark):
     return (board[7] == mark and board[8] == mark and board[9] == mark or 
        board[4] == mark and board[5] == mark and board[6] == mark or
        board[1] == mark and board[2] == mark and board[3] == mark or
        board[7] == mark and board[4] == mark and board[1] == mark or
        board[8] == mark and board[5] == mark and board[2] == mark or
        board[9] == mark and board[6] == mark and board[3] == mark or
        board[1] == mark and board[5] == mark and board[9] == mark or
        board[7] == mark and board[5] == mark and board[3] == mark)
        
#display(['X', 'X', 'O', 'O', 'O', 'X','O', 'O','X', 'O'])
#print(win_check(['X', 'X', 'O', 'O', 'O', 'X','O', 'O','X', 'O'], 'O'))

def choose_first():
  player = random.randint(1, 2)
  if player == 1:
    return "Player1 goes first"
  return "Player2 goes first"
#print(choose_first())

def space_check(board, position):
  return (board[position] == ' ')
  
my_board = ['#', ' ', 'O', 'O', ' ', 'X','O', 'O','X', 'X']

def full_board_check(board):
  for position in range(len(board)):
    if (space_check(board, position)):
      return False
  return True

def player_choice(board):
  position = 'wrong'
  while position not in list(range(1,10)) or space_check(board, position) is False:
    position = int(input("Please choose a number from 1-9: "))
    if position in list(range(1,10)):
      if space_check(board, position) is False:
        print("Sorry that position is taken")
      else:
        return position

#print(player_choice(my_board))
def replay():
  choice = 'wrong'
  while choice not in ['Y', 'N']:
    choice = input("Do you want to play again? Enter Y/N: ").upper()
  return (choice == 'Y') 
#print(replay())

print('Welcome to Tic Tac Toe!')

#"""
while True:
  #set everything up (board, who is first, choose markers X, O)
  game_board = [' '] * 10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  if turn == 'Player 1':
    print(turn + " with marker " + player1_marker + " will go first")
  else:
    print(turn + " with marker " + player2_marker + " will go first")

  

#Variable to keep game playing
  game_on = True
  while game_on:
    if turn == 'Player 1':
      #show the board
      display_board(game_board)
      #choose a position
      position = player_choice(game_board)
      #place the marker on the position
      place_marker(game_board, player1_marker, position)
      
      #check to see if player 1 won
      if win_check(game_board, player1_marker):
        display_board(game_board)
        print("Player 1 has won!")
        game_on = False
      else:
        if full_board_check(game_board):
          display_board(game_board)
          print("It's a Tie")
          game_on = False
        else:
          turn = 'Player 2'
    else:
      #player 2 turn
      #show the board
      display_board(game_board)
      #choose a position
      position = player_choice(game_board)
      #place the marker on the position
      place_marker(game_board, player2_marker, position)
      
      #check to see if player 2 won
      if win_check(game_board, player2_marker):
        display_board(game_board)
        print("Player 2 has won!")
        game_on = False
      else:
        if full_board_check(game_board):
          display_board(game_board)
          print("It's a Tie")
          game_on = False
        else:
          turn = 'Player 1'
      
  if not replay():
    print("Thanks for playing!")
    break
        #"""
