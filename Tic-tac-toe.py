from IPython.display import clear_output


def display_board(board):
  clear_output()
  print('   |   |')
  print(' '+ board[7] +' | '+ board[8]+' | ' +board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' '+ board[4] +' | '+ board[5]+' | ' +board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' '+ board[1] +' | '+ board[2]+' | ' +board[3])
  print('   |   |')

#2 Func that take player I/P

def player_input():
  
  '''
  OUTPUT = (Player1 marker,Player2 marker)
  '''

  marker = ''
  while marker !='X' and marker != 'O':
    marker = input('Player1 : Choose X or O: ').upper()
  
  if(marker=='X'):
    return ('X','O')
  else:
    return ('O','X')

#3 Func. that takes in Board list obj & assign marker to desired position

def place_marker(board,marker,position):
  board[position] = marker

#4 Check that marker has won

def win_check(board,mark):
  return ((board[7]==mark and board[8]==mark and board[9]==mark)or
         (board[4]==mark and board[5]==mark and board[6]==mark)or
         (board[1]==mark and board[2]==mark and board[3]==mark)or 
         (board[7]==mark and board[4]==mark and board[1]==mark)or 
         (board[8]==mark and board[5]==mark and board[2]==mark)or 
         (board[9]==mark and board[6]==mark and board[3]==mark)or 
         (board[7]==mark and board[5]==mark and board[3]==mark)or 
         (board[9]==mark and board[5]==mark and board[1]==mark))

#5 Decide player

import random

def choose_first():
  if random.randint(0,1)==0:
    return 'Player 2'
  else:
    return 'Player 1'

#6 Check free space at position is available on board or not

def space_check(board,position):
  return board[position] == ' '

#7 Board is Full or Not

def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i):
      return False
  return True

#8 Ask for player's next position

def player_choice(board):
  position =0
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
    position = int(input('Choose your next position :(1-9)'))
  return position 

#9  Play again 

def replay():
  return input('Do you want to play this game again ? Enter Yes or No .').lower().startswith('y')

#10 Main part to start the game 

print('Refresh yourself by playing this awesome game - TIC-TAC-TOE Game ! ')

while True:
  theBoard = [' ']*10
  display_board(theBoard)
  player1_marker,player2_marker = player_input()
  turn = choose_first()
  print(turn + ' Will go first .')
  play_game = input('Are you ready to play this game ? Enter Yes or No.')
  if play_game.lower()[0]=='y':
    game_on = True
  else:
    game_on = False

  while game_on:
    if turn == 'Player 1':
      display_board(theBoard)
      position = player_choice(theBoard)
      place_marker(theBoard,player1_marker,position)

      if win_check(theBoard,player1_marker):
        display_board(theBoard)
        print('Congratulations ! You have won the game !')
        game_on = False
      else:
        if full_board_check(theBoard):
          display_board(theBoard)
          print('The game is Tie !')
          break
        else:
          turn = 'Player 2'
    else:
    
      # Player 2 Turn 
    
      display_board(theBoard)
      position = player_choice(theBoard)
      place_marker(theBoard,player2_marker,position)

      if win_check(theBoard,player2_marker):
        display_board(theBoard)
        print('Congratulations ! You have won the game !')
        game_on = False
      else:
        if full_board_check(theBoard):
          display_board(theBoard)
          print('The game is Tie !')
          break
        else:
          turn = 'Player 1'
          
  if not replay():
    break
