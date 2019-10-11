def main():
	boardState = [
	['B','B','B','B','B','.','.','.','.','.','.','.','.','.','.','.'],
	['B','B','B','B','B','.','.','.','.','.','.','.','.','.','.','.'],
	['B','B','B','B','.','.','.','.','.','.','.','.','.','.','.','.'],
	['B','B','B','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['B','B','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','W','.','W','.','W','.','.','.','.'],
	['.','.','.','.','.','.','.','W','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','W','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','W','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','W','W'],
	['.','.','.','.','.','.','.','.','.','.','.','W','.','W','W','W'],
	['.','.','.','.','.','.','.','.','.','.','.','.','.','W','W','W'],
	['.','.','.','.','.','.','.','.','.','.','.','W','W','W','W','W'],
	['.','.','.','.','.','.','.','.','.','.','.','W','W','W','.','W']
	]

	movesGenerator(boardState, 'BLACK')

def movesGenerator(boardState, player):
	if player == 'WHITE':
		playerPawn = 'W'
	else :
		playerPawn = 'B'

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
										jumpMoves = jumpGenerator(boardState, (row + count * i, col + count * j), playerPawn)
										for eachJump in jumpMoves:
											moves[(eachJump)] = None

										count = count + 2
										
									else:
										break

	for eachmove in moves:
		print(eachmove)
		input(" 	")

def jumpGenerator(boardState, currentPosition, playerPawn):

	jumpMoves = []

	for i in range(-1, 2):
		for j in range(-1, 2):
			if currentPosition[0] + i <= 15 and currentPosition[1] + j <= 15 and currentPosition[0] + i >= 0 and currentPosition[1] + j >= 0 and currentPosition[0] + 2 * i <= 15 and currentPosition[1] + 2 * j <= 15 and currentPosition[0] + 2 * i >= 0 and currentPosition[1] + 2 * j >= 0:
				if (boardState[currentPosition[0] + i][currentPosition[1] + j] != '.' and boardState[currentPosition[0] + 2 * i][currentPosition[1] + 2 * j] == '.') :
					jumpMoves.append(("J " + str(currentPosition[0]) + "," + str(currentPosition[1]) + " " + str(currentPosition[0] + 2 * i) + "," + str(currentPosition[1] + 2 * j)))

	return jumpMoves

main()

#After every jump check all the possible jumps and not only in one direction