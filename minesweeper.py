#COMP1405-Assignment 5 Justin Chung (101144569)

GRID_SIZE = 5 #change the grid size here

def placeMines(): #Function to create a 2D list of mines
    import random
    global GRID_SIZE
    mineBoard = []
    for row in range(GRID_SIZE):
        rowBoard = []
        for column in range(GRID_SIZE):
            x = random.randint(1,10)
            if x == 1: # 1/10 chance of a mine
                rowBoard.append("x")
            else: # 9/10 chance of empty space
                rowBoard.append(" ")
        mineBoard.append(rowBoard)
    return(mineBoard)

def makeBoard(): #Function to create the game board (2D List) with "#"
    global GRID_SIZE #same size as mineBoard
    pieceboard = []
    for row in range(GRID_SIZE):
        rowBoard = []
        for column in range(GRID_SIZE):
            rowBoard.append("#")
        pieceboard.append(rowBoard)
    return(pieceboard)

def showBoard(pieceboard): #Function to show the game board as shown in example
    board = " |"
    for column in range(len(pieceboard)):
        board = board + str(column)
    board = board + "\n" + "----" + ("-"*column)
    for row in range(len(pieceboard)): #Loop that takes the 2D List from pieceBoard and turn to string
        piece = ""
        for i in range(len(pieceboard)):
            piece = piece + str(pieceboard[row][i])
        board = board + "\n" + str(row) + "|" + piece #Printing for each row of the board
        row = int(row)
    return(board)

def countHiddenCells(pieceboard): #Function to count the unrevealed cells
    count = 0
    for i in range(len(pieceboard)): #Find each cell in the 2D List with "#"
        for j in range(len(pieceboard[i])):
            if pieceboard[i][j] == "#":
                count += 1
    return(count)

def countAllMines(mineboard): #Function to count all mines in game
    count = 0
    for i in range(len(mineboard)): #Find each cell in the 2D List with mine
        for j in range(len(mineboard[i])):
            if mineboard[i][j] == "x":
                count += 1
    return(count)

def isMineAt(mineBoard,row,column): #Function that will check the inputted cell if there is a mine.
    if mineBoard[int(row)][int(column)] == "x": #If there is a mine there
        return True
    else: #If there isn't
        return False

def countAdjacentMines(mineBoard,row,column): #Function to determine the number of mines in the adjacent area
    count = 0
    if int(row) > 0 and int(column) > 0: #Top Left
        if mineBoard[int(row)-1][int(column)-1] == "x":
            count += 1
    if int(column) > 0: #Left
        if mineBoard[int(row)][int(column)-1] == "x":
            count += 1
    if int(row) < (len(mineBoard)-1) and int(column) > 0: #Bottom Left
        if mineBoard[int(row)+1][int(column)-1] == "x":
            count += 1
    if int(row) > 0: #Top
        if mineBoard[int(row)-1][int(column)] == "x":
            count += 1
    if int(row) > 0 and int(column) < (len(mineBoard)-1): #Top Right
        if mineBoard[int(row)-1][int(column)+1] == "x":
            count += 1
    if int(column) < (len(mineBoard)-1): #Right
        if mineBoard[int(row)][int(column)+1] == "x":
            count += 1
    if int(row) < (len(mineBoard)-1) and int(column) < (len(mineBoard)-1): #Bottom Right
        if mineBoard[int(row)+1][int(column)+1] == "x":
            count += 1
    if int(row) < (len(mineBoard)-1): #Bottom
        if mineBoard[int(row)+1][int(column)] == "x":
            count += 1
    return(count)

def reveal(pieceBoard,mineBoard,row,column): #Function to reveal the selected cell
    rowMax = len(pieceBoard)
    minesCell = isMineAt(mineBoard,row,column) #check if selected cell have mine
    if minesCell == True: #If there is a mine, return false and end the game
        return False
    else: #If there isn't a mine then it will determine if its a space or have adjacent mines
        adjacentMines = countAdjacentMines(mineBoard,row,column)
        if adjacentMines > 0: #If cell have adjacent mine then it will return the number of adjacent mines
            pieceBoard[row][column] = adjacentMines
        else: #If cell is a space, call it recursively with adjacent spaces
            pieceBoard[row][column] = " "
            if row + 1 < rowMax: # Check Bottom
                if pieceBoard[row+1][column] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row+1,column)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row+1,column)
            if row - 1 >= 0: #Check Top
                if pieceBoard[row-1][column] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row-1,column)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row-1,column)
            if column + 1 < rowMax: #Check Right
                if pieceBoard[row][column+1] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row,column+1)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row,column+1)
            if column - 1 >= 0: #Check Left
                if pieceBoard[row][column-1] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row,column-1)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row,column-1)
            if (row - 1 >= 0) and (column - 1 >= 0): #Check Top Left
                if pieceBoard[row-1][column-1] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row-1,column-1)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row-1,column-1)
            if (row + 1 < rowMax) and (column - 1 >= 0): #Check Bottom Left
                if pieceBoard[row+1][column-1] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row+1,column-1)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row+1,column-1)
            if (row - 1 >= 0) and (column + 1  < rowMax): #Check Top Right
                if pieceBoard[row-1][column+1] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row-1,column+1)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row-1,column+1)
            if (row + 1 < rowMax) and (column + 1  < rowMax): #Check Bottom Right
                if pieceBoard[row+1][column+1] == "#":
                    adjacentMines = countAdjacentMines(mineBoard,row+1,column+1)
                    if adjacentMines == 0:
                        reveal(pieceBoard,mineBoard,row+1,column+1)

def showMineBoard(pieceboard,mineboard): #Function to display the mines when game is lost
    for i in range(len(mineboard)):
        for j in range(len(mineboard[i])):
            if mineboard[i][j] == "x":
                pieceboard[i][j] = "X"
    return(pieceboard)

def main(): #Main function of the game
    pieceBoard = makeBoard()
    mineBoard = placeMines()
    mineCells = countAllMines(mineBoard)
    while True: #Loop until user win or lose
        print(showBoard(pieceBoard))
        while True: #Loop for the user input. Only break when the input is valid
            userInput = input("Select a cell (row,column): ")
            userInput = userInput.split(",")
            try: #Catching number inputs
                if len(userInput) == 2: #If the user input a row and column
                    row = int(userInput[0])
                    column = int(userInput[1])
                    if row >= 0 and column >= 0: #Has to be equal or greater than 0
                        if row < len(pieceBoard) and column < len(pieceBoard): #If the input is in the gameboard
                            break #Exit loop if all requirements are reached
            except ValueError: #Catching letter inputs
                print("Please enter ONLY numbers for row and column")
        flag = reveal(pieceBoard,mineBoard,row,column)
        hiddenCells = countHiddenCells(pieceBoard)
        if hiddenCells == mineCells: #If the remaining hidden cells is the same number of mines then the user win
            print(showBoard(pieceBoard))
            print("Congratulations! You Win!")
            break
        if flag == False: #If the user selected a cell with mine, it will show the cells on the pieceBoard and then the user lose
            pieceBoard = showMineBoard(pieceBoard,mineBoard)
            print(showBoard(pieceBoard))
            print("Game Over!")
            break
main()
