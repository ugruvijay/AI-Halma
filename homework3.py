
class Halma:
	def startGame(self):
		boardState = []
		player = ""
		gameType = ""
		timeRemaining = ""
		playerPawn = ""

		gameType, player, timeRemaining = self.readInputFile(boardState)

		if player == 'WHITE':
			playerPawn = 'W'
		else :
			playerPawn = 'B'

		self.movesGenerator(boardState, playerPawn)

	def readInputFile(self, boardState):
		line = ""

		with open('input.txt', 'r') as inputFile:
			line = inputFile.readline()
			count = 1
			while line:
				if count == 1:
					gameType = line.rstrip()
				elif count == 2:
					player = line.rstrip()
				elif count == 3:
					timeRemaining = float(line.rstrip())
				elif count == 4:
					for i in range(0, 16):
						boardState.append(line.rstrip())
						boardState[i] = [char for char in boardState[i]] 
						line = inputFile.readline()
				elif count == 5:
					break
				
				line = inputFile.readline()
				count += 1
		return gameType, player, timeRemaining

	def movesGenerator(self, boardState, playerPawn):
		moves = {}

		for row in range(0, 16):
			for col in range(0, 16):
				if(boardState[row][col] == playerPawn):
					for i in range(-1, 2):
						for j in range(-1, 2):
							if  row + i <= 15 and col + j <= 15 and row + i >= 0 and col + j >= 0:
								if(boardState[row + i][col + j] == '.'):
									moves[('E ' + str(row) + "," + str(col) + " " + str(row + i) + "," + str(col + j))] = None
								else:
									count = 2
									while row + count * i <= 15 and col + count * j <= 15 and row + count * i >= 0 and col + count * j >= 0:			
										if boardState[row + count * i - i][col + count * j - j] != '.' and boardState[row + count * i][col + count * j] == '.':
											moves[('J ' + str(row + (count - 2) * i) + "," + str(col + (count - 2) * j) + " " + str(row + count * i) + "," + str(col + count  * j))] = None
											jumpMoves = self.jumpGenerator(boardState, (row + count * i, col + count * j), playerPawn)
											for eachJump in jumpMoves:
												moves[(eachJump)] = 0

											count = count + 2
											
										else:
											break
		input("")

		for eachMove in moves:
			if(moves.get(eachMove) == 0):
				self.boardGenerator(boardState, playerPawn, eachMove)
				input("")

	def jumpGenerator(self, boardState, currentPosition, playerPawn):
		jumpMoves = []
		for i in range(-1, 2):
			for j in range(-1, 2):
				if currentPosition[0] + i <= 15 and currentPosition[1] + j <= 15 and currentPosition[0] + i >= 0 and currentPosition[1] + j >= 0 and currentPosition[0] + 2 * i <= 15 and currentPosition[1] + 2 * j <= 15 and currentPosition[0] + 2 * i >= 0 and currentPosition[1] + 2 * j >= 0:
					if (boardState[currentPosition[0] + i][currentPosition[1] + j] != '.' and boardState[currentPosition[0] + 2 * i][currentPosition[1] + 2 * j] == '.') :
						jumpMoves.append(("J " + str(currentPosition[0]) + "," + str(currentPosition[1]) + " " + str(currentPosition[0] + 2 * i) + "," + str(currentPosition[1] + 2 * j)))

		return jumpMoves

	def displayBoard(self, boardState):
		for i in range(0, 16):
			for j in range(0, 16):
				print(boardState[i][j] + " ", end='')
			print("\n")

	def displayAllMoves(self, moves):
		for eachmove in moves:
			print(eachmove)
			input("")

	def boardGenerator(self, boardState, playerPawn, move):
		boardAfterOneMove = [row[:] for row in boardState]

		startingPosition = move.split()[1].split(',')
		startingPosition_x = int(startingPosition[0])
		startingPosition_y = int(startingPosition[1])
		boardAfterOneMove[startingPosition_x][startingPosition_y] = '.'

		endingPosition = move.split()[2].split(',')
		endingPosition_x = int(endingPosition[0])
		endingPosition_y = int(endingPosition[1])
		boardAfterOneMove[endingPosition_x][endingPosition_y] = playerPawn

		self.displayBoard(boardAfterOneMove)

		if(playerPawn == 'B'):
			nextPlayerPawn = 'W'
		else:
			nextPlayerPawn = 'B'

#		self.movesGenerator(boardAfterOneMove, nextPlayerPawn)
#		input()

	def minimax(self, boardState, depth):
		if(depth == 0):
			return 

def main():
    halmaAgent = Halma()
    halmaAgent.startGame()

if __name__ == "__main__":
    main()
#After every jump check all the possible jumps and not only in one direction