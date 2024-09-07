import random
import time
import os
from math import ceil

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
	print("Connect k is a unlimited-player game where the")
	print("objective is to get k of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("unlimited grid. The first player to get k")
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

# check the input is numerical or not
# if not then input again
def numerical_input(prompt):
	data_input = input(prompt)
	valid = data_input.isnumeric() # check the input numerical or not
	while valid is False: # if the input not numerical, need to input again until valid is true
		print("Invalid input, please try again.")
		data_input = input(prompt)
		valid = data_input.isnumeric()
	return data_input

def create_board(row_of_game, column_of_game):
	output = []
	for i in range(row_of_game): # run a outer list that got n row (input by player)
		output.append([0]*column_of_game) # run a inner that got n column (input by player)
	return output

def print_board(board, row_of_game, column_of_game, player_list):
	string = ''
	for num in range(column_of_game - 1):
		if num == 1:
			string += "====="
		elif num == int((column_of_game/2) - 1):
			string += "connectk"
		else:
			string += "===="
	print(string)
	string = ""
	for player in player_list:
		string += f"Player {player}: {player}  "
	print(string)
	print("")
	string = ""
	# use for loop to print 1 ~ column that the player input
	for num in range(1, column_of_game + 1): 
		if num == column_of_game or num >= 10:
			string+= f"  {num}"
		else:
			string+= f"  {num} "
	print(string)
	string = ""
	# use for loop to create the dotted line
	for num in range(column_of_game):
		string += f" ---"
	print(string)
	for row in range(row_of_game):
		upper_layer = "|"
		lower_layer = ""
		for column in range(column_of_game):
			num = board[row][column]
			if num == 0:
				output = " " # if the no piece dropped, the output space
			else:
				output = num # if got piece then output the player number that drop there
			upper_layer += f" {output} |"
			lower_layer += " ---"
		print(upper_layer)
		print(lower_layer)
	string = ""
	# print number at bottom to easy to look if the too much of row
	for num in range(1, column_of_game + 1): 
		if num == column_of_game or num >= 10:
			string+= f"  {num}"
		else:
			string+= f"  {num} "
	print(string)
	string = ""
	# print = and the length fit the length of the board
	for num in range(column_of_game):
		if num == 1:
			string += "====="
		else:
			string += "===="
	print(string)

def drop_piece(board, player, row_of_game, column_of_game):
	i = row_of_game - 1 # bottom row = row_of_game - 1
	while i >= 0: # check whether the board is full or not and drop the piece into the board
		if board[i][column_of_game - 1] == 0:
			board[i][column_of_game - 1] = player
			return True
		i -= 1
	return False # if the board cannot drop, then return False

def execute_player_turn(player, board, row_of_game, column_list):
	while True: # the loop will continue run until break
		# check whether the player drop valid or not
		player_drop = int(validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ", column_list))
		drop_valitidy = drop_piece(board, player, row_of_game, player_drop) # check the column full or not and drop
		if drop_valitidy == True:
			break # if drop successful then break
		else:
			print("That column is full, please try again.") # if not successful, request for another drop
	return player_drop # return the column that the player drop

def end_of_game(board, number_k):
	move = [[1,0], [0,1], [1,1], [-1, 1]]
	for row in range(len(board)):
		for column in range(len(board[0])):
			check1 = board[row][column]
			count = 0
			for move_n in range(4):
				dy = move[move_n][0]
				dx = move[move_n][1]
				count = 0
				for n in range(1,number_k): # n is the number need to check, k pieces connect then need to check k piece in all direction
					y = row + n * dy
					x = column + n * dx
					if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):          
						check2 = board[y][x]
						if check1 == check2 and check2 != 0:
							count += 1
							if count == number_k - 1: # count = k - 1 mean k in a line
								return check2
						else:
							break
						
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 0:
				return 0
	return -1

def local_k_player_game():
	# numerical_input() is used to check whether the player input a number
	# if not then input again
	row_of_game = int(numerical_input("Please input the row of the game: ")) # row of the board
	while row_of_game <3:
		print("Minimun 3 row :(")
		row_of_game = int(numerical_input("Please input the row of the game: "))
	column_of_game = int(numerical_input("Please input the column of the game: "))
	while column_of_game <3:
		print("Minimun 3 column :(")
		column_of_game = int(numerical_input("Please input the row of the game: "))
	column_list = []
	# create a column_list to use at code below
	for num in range(1, column_of_game + 1):
		column_list.append(str(num))
	number_k = int(validate_input("Please input the number of connection to win: ", column_list)) # to make sure the line to win not excess column
	while number_k < 3:
		print("Minimum 3 in a line to win :(")
		number_k = int(validate_input("Please input the number of connection to win: ", column_list))
	player_number = int(numerical_input("Please input player numbers: ")) # input player number
	while player_number < 2 or player_number > 9:
		print("Minimun 2 player :(, Maximun 9 player:(")
		player_number = int(numerical_input("Please input player numbers: "))
	board = create_board(row_of_game, column_of_game)
	player_list = [] # player_list to run player turn in for loop below
	for num in range(1, player_number + 1):
		player_list.append(str(num))
	print_board(board, row_of_game, column_of_game, player_list)
	for round_play in range(len(board) * len(board[0])): # run the game 
		end = 0
		for player in player_list: # run player in the list
			drop_column = execute_player_turn(player, board, row_of_game, column_list)
			clear_screen()
			print_board(board, row_of_game, column_of_game, player_list)
			print(f"Player {player} dropped a piece into column {drop_column}")
			end = end_of_game(board, number_k)
			if end != 0:
				if end != -1:
					print(f"PLayer {end} wins!!!!")
				else: 
					print("Draw game......")
				return

def display_main_menu():
	print("=============== Main Menu ===============")
	print("Welcome to Connect k!")
	print("1. View Rules")
	print("2. Play a local k player game")
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
			local_k_player_game()

		# if option 3 is selected, programme will go to solo mode against cpu
		elif option == 3:
			game_against_cpu()

		# if an invalid number is selected, programme will display an invalid input
		else:
			print("Invalid input")
		
		print()

def cpu_player_easy(board, player, row_of_game, column_of_game):
	random_column = random.randint(1, column_of_game) # random generate a number between 1 to the number of column that the player input
	while board[0][random_column-1] != 0: # check the column full or not, if full then generate a new number
		randon_column = random.randint(1, column_of_game)
	drop_piece(board, player, row_of_game, random_column) # drop to the column
	return random_column

def cpu_player_medium(board, player, column_of_game, player_list, row_of_game, number_k):
	for column in range(1, column_of_game + 1): # try to drop to every column
		valid_drop = drop_piece(board, player, row_of_game, column)
		if valid_drop == True:
			end = end_of_game(board, number_k)
			if end == player: # check can win or not
				return column
			else:
				for row in range(len(board)): # cannot win, change back to the original board
					if board[row][column-1] != 0:
						board[row][column-1] = 0
						break
	# check opponent can win in the next turn or not
	for column in range(1, column_of_game + 1):
		for opponent in player_list:
			if opponent != player: # player in the list include the cpu, need to exclude it 
				valid_drop = drop_piece(board, opponent, row_of_game, column) # try to drop opponent to each column
				if valid_drop == True:
					end = end_of_game(board, number_k)
					if end == opponent: # if opponent can win, then drop to the column to block the win
						for row in range(len(board)):
							if board[row][column-1] != 0:
								board[row][column-1] = player
								return column
					else:
						for row in range(len(board)): # cannot win, change back to the original board
							if board[row][column-1] != 0:
								board[row][column-1] = 0
								break
	drop = cpu_player_easy(board, player, row_of_game, column_of_game) # all player cannot win then random generate a number
	return drop

# similar strategy with medium, but will not random generate number
def check_win(board, player, column_of_game, player_list, row_of_game, number_k):
	for column in range(1, column_of_game + 1):
		valid_drop = drop_piece(board, player, row_of_game, column)
		if valid_drop == True:
			end = end_of_game(board, number_k)
			if end == player:
				return column
			else:
				for row in range(len(board)):
					if board[row][column-1] != 0:
						board[row][column-1] = 0
						break

	for column in range(1, column_of_game + 1):
		for opponent in player_list:
			if opponent != player:
				valid_drop = drop_piece(board, opponent, row_of_game, column)
				if valid_drop == True:
					end = end_of_game(board, number_k)
					if end == opponent:
						for row in range(len(board)):
							if board[row][column-1] != 0:
								board[row][column-1] = player
								return column
					else:
						for row in range(len(board)):
							if board[row][column-1] != 0:
								board[row][column-1] = 0
								break

	return False

def cpu_player_hard(board, player, column_of_game, player_list, row_of_game, number_k):
	valid = check_win(board, player, column_of_game, player_list, row_of_game, number_k) # check whether got player can win or not, if cpu can win then cpu put that column, other player can win then block the player win
	if valid == False: # if all player cannot win, calculate the score
		score_list = [] # list to be appended the score of each column
		for column in range(1, len(board[0])+1):
			score = 0
			for opponent in player_list: # calculate the surrounding piece
				valid_drop = drop_piece(board, opponent, row_of_game, column)
				if valid_drop == True:
					for i in range(row_of_game): # to find the row that the piece drop
						row = 0
						if board[i][column - 1] != 0:
							row = i
							break
					move = [[-1, -1], [0, -1], [1, -1], [1, 0], [1,1], [0, 1], [-1, 1]]
					check1 = board[row][column - 1] # the centre (the drop piece)
					for move_index in range(len(move)): # the direction of calculating
						for n in range(number_k): # the max number that the piece can in a line is number_k, so check until number_k - 1
							y = row + n * move[move_index][0] 
							x = column - 1 + n * move[move_index][1]
							if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
								check2 = board[y][x]
								if check1 == check2:
									score += (n + 1) # the number of piece in a line more close to number_k, add more score
								else:
									break
					board[row][column - 1] = 0 # change back to the original board
					if opponent == player: # only add this score when check the player move, as this is a win strategy 
						if column == ceil(column_of_game/2): # at the middle column, add 3 mark, round up the column/2 to find middle column
							score += 3
						elif column == ceil(column_of_game/2 + 1): # column on the side of middle add 1 mark
							score += 1
						elif column == ceil(column_of_game/2 - 1):
							score += 1
					else:
						if row - 1 >= 0: # if opponent cna win after cpu dropping this column, score will - 10
							board[row - 1][column - 1] = opponent
							end = end_of_game(board, number_k)
							if end == opponent:
								score = -10
							board[row - 1][column - 1] = 0
				else: 
					score = -100 # the column is full
			score_list.append(score) # append each score into the score_list
		max_score = max(score_list) # find the max score of the from the list
		for column in range(1, len(score_list) + 1): # find the max score at which column
			if max_score == score_list[column - 1]:
				drop_piece(board, player, row_of_game, column) # drop the piece to the column which has the highest mark
				return column
	else:
		return valid # Valid = True

def game_against_cpu():
	
	row_of_game = int(numerical_input("Please input the row of the game: ")) # row of the board
	while row_of_game <3: # prevent the player input too less row, min 3
		print("Minimun 3 row :(")
		row_of_game = int(numerical_input("Please input the row of the game: "))

	column_of_game = int(numerical_input("Please input the column of the game: "))
	while column_of_game <3: # to prevent the player input too less column, min 3
		print("Minimun 3 column :(")
		column_of_game = int(numerical_input("Please input the row of the game: "))

	column_list = [] # append the column to a list
	# create a column_list to use at code below
	for num in range(1, column_of_game + 1):
		column_list.append(str(num))

	number_k = int(validate_input("Please input the number of connection to win: ", column_list)) # to make sure the line to win not excess column
	while number_k < 3: # prevent the number of piece in a line too less
		print("Minimum 3 in a line to win :(")
		number_k = int(validate_input("Please input the number of connection to win: ", column_list))
	
	total_player = 10
	while total_player > 9:
		player_number = int(numerical_input("Please input number of local player: ")) # input player number
		while player_number < 1: # prevent the player enter number of player that less than 2
			print("Minimun 1 player :(")
			player_number = int(numerical_input("Please input number of local player: "))

		cpu_number = int(numerical_input("Please input the number of CPU: ")) # cpu_numbe rfor player to input
		while cpu_number < 1: # At least 1 cpu
			print("Minimun 1 CPU :(")
			cpu_number = int(numerical_input("Please input the number of CPU: "))
		total_player = player_number + cpu_number
		if total_player > 9:
			print("Total player number should not exceed 9")

	cpu_level = [] # list to save the cpu level of each cpu
	player_list = []
	for num in range(1, player_number + cpu_number + 1): # create a list that contain all playe including cpu
		player_list.append(num)
	board = create_board(row_of_game, column_of_game)
	print("Difficulty Level of cpu: ") # choose difficulty
	print("1. Easy")
	print("2. Medium")
	print("3. Hard")
	for cpu in range(cpu_number):
		cpu_difficulty = int(validate_input(f"Please select a cpu level for cpu {cpu+1}: ", ["1", "2", "3"]))
		cpu_level.append(cpu_difficulty) # sva the difficulty into the cpu level list
	clear_screen()
	print_board(board, row_of_game, column_of_game, player_list)
	for round_play in range(len(board) * len(board[0])): # run the game
		end = 0
		for player in range(1, player_number + 1): # fisrt local player (1) to last local player (player_number+1) in player_list
			drop_column = execute_player_turn(player, board, row_of_game, column_list)
			clear_screen()
			print_board(board, row_of_game, column_of_game, player_list)
			print(f"Player {player} dropped a piece into column {drop_column}")
			end = end_of_game(board, number_k)
			if end != 0:
				if end != -1:
					print(f"Player {end} wins!!!!")
				else:
					print("Draw game......")
				return
		for player in range(player_number + 1, len(player_list) + 1): # first cpu to last cpu in player_list
			if cpu_level[player - player_number - 1] == 1: # the first cpu in the player_list is player - player_number - 1, then value will be 0, the first cpu level in the list is 0
				drop_column = cpu_player_easy(board, player, row_of_game, column_of_game)
			if cpu_level[player - player_number - 1] == 2:
				drop_column = cpu_player_medium(board, player, column_of_game, player_list, row_of_game, number_k)
			if cpu_level[player - player_number - 1] == 3:
				drop_column = cpu_player_hard(board, player, column_of_game, player_list, row_of_game, number_k)
			clear_screen()
			print_board(board, row_of_game, column_of_game, player_list)
			print(f"Player {player} dropped a piece into column {drop_column}")
			time.sleep(2) # slow down the game 
			end = end_of_game(board, number_k)
			if end != 0:
				if end != -1:
					print("CPU wins :) !!!!!")
				else:
					print("Draw game......")
				return


main()

















