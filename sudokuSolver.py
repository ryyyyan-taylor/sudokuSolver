import random
import sys

def generateSudoku(): 
	maxAttempts = 100 #stops the program after 100 attempts
	count = 9999
	solCount = 0

	while count > maxAttempts:
	    solCount +=1
	    
	    puzzle = []
	    for i in range(9):
	        row = []
	        for j in range(9):
	            row.append(0)
	        
	        puzzle.append(row)

	    for row in range(9):
	        for col in range(9):
	            
	            thisRow=puzzle[row]
	            thisCol=[]
	            
	            for h in range(9):
	                thisCol.append(puzzle[h][col])

	            subCol = int(col/3)
	            subRow = int(row/3)
	            subMat = []
	            
	            for subR in range (3):
	                for subC in range (3):
	                    subMat.append(puzzle[subRow*3 + subR][subCol*3 + subC])
	            
	            randVal = 0
	            count = 0
	            while randVal in thisRow or randVal in thisCol or randVal in subMat:
	                randVal = random.randint(1,9)
	                count+=1

	                if count > maxAttempts: break 
	            
	            puzzle[row][col] = randVal

	            if count > maxAttempts: break 
	        
	        if count > maxAttempts: break

	nums = 81
	while nums >= (int(sys.argv[1]) + 1):
		
		randI = random.randint(0,8)
		randJ = random.randint(0,8)
		
		if(puzzle[randI][randJ]):
			puzzle[randI][randJ] = 0
			nums -= 1

	return puzzle

def printSudoku(sudoku):

	for i in range(len(sudoku)):
		line = ""
		if i == 3 or i == 6: print("---------------------")
		
		for j in range (len(sudoku[i])):
			
			if j == 3 or j == 6 : line += "| "
			if sudoku[i][j] == 0 :
				line += "  "
				continue
			line += str(sudoku[i][j]) + " "
		
		print(line)

def findNextCellToFill(sudoku):

	for x in range(9):
		for y in range(9):
			if sudoku[x][y] == 0: return x, y
	return -1, -1

def isValid(sudoku, i, j, e):
	
	goodRows = all([e != sudoku[i][x] for x in range (9)])
	if goodRows:
		
		goodColumns = all([e != sudoku[x][j] for x in range (9)])
		if goodColumns:

			secTopX, secTopY = 3 * (i//3), 3 * (j//3)
			
			for x in range (secTopX, secTopX + 3):
				for y in range (secTopY, secTopY + 3):
					if sudoku[x][y] == e: return False
			
			return True
	return False

def solveSudoku(sudoku, i = 0, j = 0):

	i, j = findNextCellToFill(sudoku)
	if i == -1: return True

	for e in range (1, 10):
		if isValid(sudoku, i, j, e):
			sudoku[i][j] = e

			if solveSudoku(sudoku, i, j): return True
			sudoku[i][j] = 0

	return False

def main():
	sudoku = generateSudoku()
	printSudoku(sudoku)
	solveSudoku(sudoku)
	print("\n\n")
	printSudoku(sudoku)

main()