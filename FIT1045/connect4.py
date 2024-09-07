import random
import time
import os

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')

def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""

	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")

def validate_input(prompt, valid_inputs):
	data_input = input(prompt)
	#check input in list or not
	while data_input not in valid_inputs:
		# if the input out of the list, 
		# the player need to enter a input again until the input is in the list and quit the while loop
		# otherwise the while loop while keep runing
		print("Invalid input, please try again.")
		data_input = input(prompt)
	# the function will return the input that the player enter, which will be the column afterward
	return data_input

def create_board():
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	outer_list = []
	# for loop will run 6 time and create the inner list
	# [0] * 7 will create a inner list that contain seven 0 in the list
	# the inner list is appended into the outer_list
	for row in range(6):
		outer_list.append([0]*7)
	# this function return a outer_list that contain 6 inner_list
	# and each inner list contain 7 elements which is 0
	return outer_list

def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""

	print("========== Connect4 =========")
	print("Player 1: X       Player 2: O")
	print("")
	string = ""
	# use for loop to print 1~7
	for num in range(1,8): 
		if num == 7:
			string+= f"  {num}"
		else:
			string+= f"  {num} "
	print(string)
	string = ""
	# use for loop to create the dotted line
	for num in range(7):
		string += f" ---"
	print(string)
	# use for loop to create 12 row
	for row in range(6):
		# run 6 row
		# the 6 row contain upper layer - which the compile
		# lower layer which is ---
		upper_layer = "|"
		lower_layer = ""
		for column in range(7):
			piece_num = board[row][column]
			# check the column is 0, 1 or 2. if 0 print (space) in the cell, 1 print X, 2 print O
			# combine the (space) or X or O and | into a string
			if piece_num == 0:
				output = " "
			elif piece_num == 1:
				output = "X"
			elif piece_num == 2:
				output = "O"
			upper_layer += f" {output} |"
			lower_layer += " ---"
		print(upper_layer)
		print(lower_layer)
	string = ""
	for num in range(29):
		string += f"="
	print(string)

def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# use of while loop to check the column can be drop or not
	# check from the bottom, if the cell(board[row][column - 1]) is 0, so that can be drop.
	# and the function return True, which mean it is a successful drop 
	# if the cell is 1 or 2, will move to the upper row to check can drop or not,
	# until the top row (row = 0)
	# if the cell of the top row is 1 or 2 (board[0][column - 1] = 1/2) 
	# means the column is full and the function will return false, which mean it is not a successful drop
	row = 5
	while row >= 0:
		if board[row][column-1] == 0:
			board[row][column-1] = player
			return True
		row -= 1
	return False

def execute_player_turn(player, board): # Task 5
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	# combiner of validate_input and drop_piece function
	# validate_input function: promp is asking the player to drop a piece and check the column that the player drop valid or not
	# drop_piece: use the output(column) from validate_input to drop into the board and check whether the column is full or not
	run = True
	# run will also True until the player input a valid input into a valid column
	while run == True:
		player_drop = int(validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"]))
		# drop_valitidy is the output of drop_piece 
		# if it is a successful drop, drop_valitidy will be True and break the while loop
		drop_valitidy = drop_piece(board, player, player_drop)
		if drop_valitidy == True:
			break
		# if drop_valitidy is False then the while loop will continue and request for a valid input
		else:
			print("That column is full, please try again.")
	return player_drop

def end_of_game(board):
	# end of game is checked by checking the row, column, slash and backslash of each cell
	# move contain a list of the checking directions
	# the inner list represent as [y-direction(row), x-directon(column)]
	# [1,0] will check the upper cell of the cell, so it check the row
	# [0,1] check the column, [1,1]check slash, [-1,1] check backslash
	move = [[1,0], [0,1], [1,1], [-1, 1]]
	for row in range(len(board)):
		for column in range(len(board[0])):
			# use two for loop to run all the cel
			check1 = board[row][column] 
			# check1 is the centre cell to check
			# count is used to count how many same piece in a line
			for move_n in range(4):
				# move_n used to run the list
				# dx and dy is the different of two 
				count = 0
				for n in range(1,4):
					# n is the number that need to check
					# need to check the 3 cell from the centre cell
					# dy represent the different in row of the cell from the centre cell
					# dx represent the different in column of the cell from the centre cell
					dy = n * move[move_n][0] 
					dx = n * move[move_n][1]
					# y is the final row of the cell
					# x is the final column of the cell
					y = row + dy
					x = column + dx
					if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
						check2 = board[y][x]
						# check 2 is the cell 
						# check whether the cell is same as the centre cell or not
						# if yes, count + 1 and then continue check the thrid and forth cell
						# if not , then break the loop, and go for the next direction
						if check1 == check2 and check2 != 0:
							count += 1
							if count == 3:
								# if count = 3, mean that 4 in a line, so the player win
								# the function return the winner
								return check2
						else:
							break
						
	# if no player win then the function will check whether all the cell of the board has been drop
	# if the cell of board contain 0, means still got place to drop and the game can continue, return 0
	# if the cell of board only contain 1/2, means the board is full and is a draw game, return 3
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 0:
				return 0
	return 3

def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# the for loop will run the game until a player win or draw
	# end of the game will be determined by the function end_of_game
	# if end = 0, means no player win and no draw, the loop will continue run]
	# if end = 1, means player 1 win, 2, means player 2 win and the function will return the winner
	# if end = 3 menas draw game and the function will return 3
	board = create_board()
	print_board(board)
	for game_round in range(len(board)*len(board[0])):
		# game_round is the round of the game
		# first turn is player 1 and in round 0, so the even number game_round is player 1
		# second turn is player 2 and in round 1, so the old number game_round is player 2
		if game_round % 2 == 0:
			player = 1
		else:
			player = 2
		# function execute_player_turn is used to let the player to input the column
		drop_column = execute_player_turn(player, board)
		clear_screen()
		print_board(board)
		print(f"Player {player} dropped a piece into column {drop_column}")
		end = end_of_game(board)
		if end != 0:
			if end != 3:
				print(f"Player {end} wins!!!!")
			else:
				print("Draw game.....")
			return end


def display_main_menu():
	print("=============== Main Menu ===============")
	print("Welcome to Connect 4!")
	print("1. View Rules")
	print("2. Play a local 2 player game")
	print("3. Play a game against the computer")
	print("4. Exit  ")
	print("=========================================")

def main():
	"""
	Defines the main loop that allows the player to start a game, view rules or quit.
	"""

	while True:
		display_main_menu()
		option = int(validate_input("Please enter an option: ", ["1", "2", "3", "4"]))
		clear_screen()
		
		# If option 4 is selected, break out of loop and quit
		if option == 4:
			print("Exiting game")
			break

		# if option 1 is selected, programme will display the rules of the game
		if option == 1:
			print_rules()

		# if option 2 is selected, programme will go to local 2 player mode
		elif option == 2:
			local_2_player_game()

		# if option 3 is selected, programme will go to solo mode against cpu
		elif option == 3:
			game_against_cpu()

		# if an invalid number is selected, programme will display an invalid input
		else:
			print("Invalid input")
		
		print()

def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# random generate a number between 1-7, and drop into the column
	column = random.randint(1,7)
	# check whether the column generated can drop or not(full or not) 
	# if full generate a another column until it is a valid drop 
	while board[0][column-1] != 0:
		column = random.randint(1,7)
	drop_piece(board, player, column)
	return column

def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty.
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# try to drop to each column to check whether can win or not if drop to that column
	for column in range(1, len(board[0])+1):
		valid_drop = drop_piece(board, player, column)
		if valid_drop == True:
			end = end_of_game(board)
			# if can win then return the column 
			if end == player:
				return column
			# if cannot win then change the cell back to 0
			else:
				for row in range(len(board)):
					if board[row][column - 1] != 0:
						board[row][column - 1] = 0
						break
	
	# try to drop oppenent piece to each column to check whether opponent can win at the next round or not
	for column in range(1, len(board[0])+1):
		if player == 1:
			opponent = 2
		else:
			opponent = 1 

		valid_drop = drop_piece(board, opponent, column)
		if valid_drop == True:
			end = end_of_game(board)
			# if opponent can win by dropping to that column, then cpu will drop at that column
			if end == opponent:
				for row in range(len(board)):
					if board[row][column-1] != 0:
						board[row][column-1] = player
						return column
			# if not, change the cell back to 0 
			else:
				for row in range(len(board)):
					if board[row][column-1] != 0:
						board[row][column-1] = 0
						break
	# if cpu cannot win at this round, opponent also cannot win at next round
	# cpu will random generate a column to drop_piece
	# by using previous function cpu_player_easy
	column = cpu_player_easy(board, player)
	return column

# use for cpu_player_hard
# use strategy from cpu_player_medium
# check cpu can win in this round or opponent can win in next round 
# if no, then return False
def check_win(board, player):
	for column in range(1, len(board[0])+1):
		valid_drop = drop_piece(board, player, column)
		if valid_drop == True:
			end = end_of_game(board)
			if end == player:
				return column
			else:
				for row in range(len(board)):
					if board[row][column - 1] != 0:
						board[row][column - 1] = 0
						break
	
	for column in range(1, len(board[0])+1):
		if player == 1:
			opponent = 2
		else:
			opponent = 1 
		valid_drop = drop_piece(board, opponent, column)
		if valid_drop == True:
			end = end_of_game(board)
			if end == opponent:
				for row in range(len(board)):
					if board[row][column - 1] != 0:
						board[row][column - 1] = player
						return column
			else:
				for row in range(len(board)):
					if board[row][column - 1] != 0:
						board[row][column - 1] = 0
						break
	return False

def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.

	The cpu will check whether can win in this round or oppenent will win at next round(same as medium)
	But cpu will not random drop if False to both statement above
	Cpu will drop according a scoring mechanism
	The cpu will calculate the score of dropping to each column, 
	and drop to the column that has highest score
	The score will given according to the surrounding pieces 
	Drop to centre (column = 4): + 3 mark
	Drop at middle (column = 3,5): + 1 mark
	One own piece at surrounding: + 2 mark 
	One opponent piece at surrounding: + 1 mark
	Two own piece in a line at surrounding: + 3 mark
	Two opponent piece in a line at surrounding: + 4 mark
	If after dropping to this column, opponent will win at next round: score = 0

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: None
	"""
	if player == 1:
		opponent = 2
	else:
		opponent = 1
	valid = check_win(board, player)
	# if check_win False, then calculate the score of each column
	if valid == False:
		score_list = [] # create a list to save score of each column
		for column in range(1, len(board[0])+1):
			score = 0 # start from 0 mark
			valid_drop = drop_piece(board, player, column)
			# if the drop ot the column is true, then start calculate the mark
			# if not true, then the score will be -100, to make sure cpu will not drop there as the column alr full
			if valid_drop == True: 
				# if score at centre(4) +3, middle(3,5) +1
				if column == 4:
					score += 3
				elif column == 3:
					score += 1
				elif column == 5:
					score += 1
				# find the row of the drop piece
				for i in range(len(board)):
					if board[i][column - 1] != 0:
						row = i
						break
				# check the surrounding ([y-direction, x-direction], y is the row, x is the column)
				# [-1,-1] upper left, [0,-1] left, [1,-1] lower left, [1,0] down, [1,1] lower right, [0,1] right, [-1,1] upper right
				move = [[-1, -1], [0, -1], [1, -1], [1, 0], [1,1], [0, 1], [-1, 1]]
				# the piece that drop = check1
				check1 = board[row][column - 1]
				# run each list in move
				for move_index in range(len(move)):
					y = row + move[move_index][0]
					x = column - 1 + move[move_index][1]
					# prevent the number out of board
					if y >= 30 and y < len(board) and x >= 0 and x < len(board[0]):
						# check2 is the surrounding piece
						check2 = board[y][x]
						# if the surrounding piece is own piece then +1
						if check1 == check2:
							score += 1
							# check one more move, to check whether 3 in a line or not
							y = row + 2 * move[move_index][0]
							x = column - 1 + 2 * move[move_index][1]
							if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
								check3 = board[y][x]
								# if 3 in a line, +3
								if check1 == check3:
									score += 3	
				board[row][column - 1] = 0 # change the testing piece back to 0
			valid_drop = drop_piece(board, opponent, column) #drop opponent piece to check opponent can 2 in a line or 3 in a line
			if valid_drop == True:
				for i in range(len(board)):
					if board[i][column - 1] != 0:
						row = i
						break
				move = [[-1, -1], [0, -1], [1, -1], [1, 0], [1,1], [0, 1], [-1, 1]]
				check1 = board[row][column - 1]
				for move_index in range(len(move)):
					y = row + move[move_index][0]
					x = column - 1 + move[move_index][1]
					if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
						check2 = board[y][x]
						# if can two in a line then +1 mark
						if check1 == check2:
							score += 2
							y = row + 2 * move[move_index][0]
							x = column - 1 + 2 * move[move_index][1]
							# if can 3 in a line +4 mark
							if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
								check3 = board[y][x]
								if check1 == check3:
									score += 4	
				# change the board back to origin
				board[row][column - 1] = 0
				# check whether opponent can win or not at the upper row
				# if can win then score = 0, will be the least likely drop for the cpu
				if row - 1 >= 0:
					board[row - 1][column - 1] = opponent
					end = end_of_game(board)
					if end == opponent:
						score = 0
					board[row - 1][column - 1] = 0
			else:
				score = -100
			score_list.append(score) # append each score into the score_list
		max_score = max(score_list) # find the max score of the from the list
		# find the column of the max score and drop
		for column in range(1, len(score_list) + 1):
			if max_score == score_list[column - 1]:
				drop_piece(board, player, column)
				return column
	# return valid (if cpu can win or block opponent win)
	else:
		return valid

def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	board = create_board()
	print("Difficulty Level of cpu: ")
	print("1. Easy")
	print("2. Medium")
	print("3. Hard")
	# let player to input a level
	difficulty = int(validate_input("Please select a level: ", ["1", "2" ,"3"]))
	print_board(board)
	for game_round in range(len(board) * len(board[0])):
		# if player_turn == 1:
		if game_round % 2 == 0: # first round game_round = 0, so player one is even number, cpu is odd number
			drop_column = execute_player_turn(1, board) # player drop a piece
			player = 1 # save to print at below
			clear_screen()
		else:
			# from the difficulty that player input, run a cpu
			if difficulty == 1:
				cpu = cpu_player_easy(board, 2)
			elif difficulty == 2:
				cpu = cpu_player_medium(board, 2)
			else:
				cpu = cpu_player_hard(board, 2)
			drop_column = cpu # save to print at below
			player = 2
		print_board(board)
		print(f"Player {player} dropped a piece into column {drop_column}")
		time.sleep(1)
		# check whether got player win or not
		end = end_of_game(board)
		# if player 1, the function will return 1, cpu win function return 2, draw game return 3, game continue return 0
		if end != 0:
			if end == 1:
				print("Player 1 win!!!")
			elif end == 2:
				print("CPU win :) !!!!")
			else:
				print("Draw game.....")
			return end

if __name__ == "__main__":
	main()
