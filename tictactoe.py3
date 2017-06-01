import os
import math
os.system('cls' if os.name == 'nt' else 'clear')

Board = []

def BoardMatrix():
	y=1
	x = []
	for j in range(3):
		_ = []
		for i in range(3):
			_.append(str(y))
			y+=1
		x.append(_)
	return x

def PrintBoard():
	board=''
	for z in range(3):
		board=''
		for t in range(3):
			board+=str(Board[z][t])
		print(board)

def PrettyBoard(board):
	print('   |   |')
	print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
	print('___|___|___')
	print('   |   |')
	print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
	print('___|___|___')
	print('   |   |')
	print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
	print('   |   |')
	

def VPosition(num):
	_ = math.ceil(num/3) - 1
	return _

def HPosition(num):
	_ = num%3-1
	if _ == -1:
		_ = 2
	return _

def Winner(board):
	H1 = str(board[0][0]+board[0][1]+board[0][2])
	H2 = str(board[1][0]+board[1][1]+board[1][2])
	H3 = str(board[2][0]+board[2][1]+board[2][2])
	V1 = str(board[0][0]+board[1][0]+board[2][0])
	V2 = str(board[0][1]+board[1][1]+board[2][1])
	V3 = str(board[0][2]+board[1][2]+board[2][2])
	D1 = str(board[0][0]+board[1][1]+board[2][2])
	D2 = str(board[0][2]+board[1][1]+board[2][0])
	if H1 == 'XXX' or H2 == 'XXX' or H3 ==  'XXX' or V1 == 'XXX' or V2 == 'XXX' or V3 == 'XXX' or D1 == 'XXX' or D2 == 'XXX':
		return 'X is the WINNER!!!'
	elif H1 == 'OOO' or H2 == 'OOO' or H3 ==  'OOO' or V1 == 'OOO' or V2 == 'OOO' or V3 == 'OOO' or D1 == 'OOO' or D2 == 'OOO':
		return 'O is the WINNER!!!'
	else:
		used_set = set()
		used_set.add(board[0][0])
		used_set.add(board[0][1])
		used_set.add(board[0][2])
		used_set.add(board[1][0])
		used_set.add(board[1][1])
		used_set.add(board[1][2])
		used_set.add(board[2][0])
		used_set.add(board[2][1])
		used_set.add(board[2][2])
		return str(len(used_set))


Board = BoardMatrix()

print('*************************')
PrettyBoard(Board)

# PrintBoard()
print('*************************')
i=-1
player = 'X'
while i!=0:
	move = int(input('What is your move ' + player + ' (1-9) (0 to quit)?\n'))
	i=move
	if i != 0 and Board[VPosition(move)][HPosition(move)] != 'X' and Board[VPosition(move)][HPosition(move)] != 'O':
		Board[VPosition(move)][HPosition(move)] = player
		if player == 'X':
			player = 'O'
		else:
			player = 'X'
	elif i != 0:
		print ('Try another move ' + Board[VPosition(move)][HPosition(move)] + ' is already there.')
	# PrintBoard()
	PrettyBoard(Board)
	print(Winner(Board))
	if Winner(Board) == '2':
		print ('Tie game')
		# i = 0
		Board = BoardMatrix()
		PrettyBoard(Board)
	if Winner(Board) == 'X is the WINNER!!!' or Winner(Board) == 'O is the WINNER!!!':
		i = 0
