
gridCell = [" - "," X "," O "]
gridSize = 3

def printGrid(seedInput, roundNum): # takes in a seed of 9 numbers between 1 and 3 for the indices of gridCell

    total = 0
    seedIndices = [x for x in str(seedInput)] # converts seed number into list
    seedOutput = ""
    
    print("===============")
    print(f"Y   Round #{roundNum}", end="\n\n")
    for y in range(0,gridSize): # defines the y axis of grid
        print(f"{y + 1}  ", end="")
        for x in range(0,gridSize): # defines x axis of grid
            
            index = int(seedIndices[total]) - 1

            seedOutput = f"{seedOutput}{index + 1}"
            print(gridCell[index], end="")
            total += 1 # gets the total number of iterations
        print("\n")
    print("    1  2  3   X")
    print("===============")

    return(seedOutput)

def seedNumToList(seedInput): # converts a 9 number seed to a nested list of x and y values
    indices = [x for x in str(seedInput)]
    y1 = indices[0:3]
    y2 = indices[3:6]
    y3 = indices[6:9]
    seedOutput = [y1,y2,y3]

    return(seedOutput)

def seedListToNum(seedList): # converts a nested list of x and y values into a 9 number seed
    num = ""
    for y in range(0,gridSize):
        for x in range(0,gridSize):
            num = f"{num}{seedList[y][x]}"

    return(int(num))

def seedWon(seedList): # returns true or false

    # creates groups for the rows of the grid
    y1 = seedList[0]
    y2 = seedList[1]
    y3 = seedList[2]

    # creates groups for the columns of the grid
    x1 = [y1[0],y2[0],y3[0]]
    x2 = [y1[1],y2[1],y3[1]]
    x3 = [y1[2],y2[2],y3[2]]
    
    # creates groups for the diagonals of the grid
    z1 = [y1[0],y2[1],y3[2]]
    z2 = [y1[2],y2[1],y3[0]]

    win = False


    if "1" not in set(y1): # makes sure all cells in row 1 are being used by X or O
        if (len(set(y1)) == 1): # checks to see if all elements of row 1 are same = win
            win = True
    if "1" not in set(y2): # makes sure all cells in row 2 are being used by X or O
        if (len(set(y2)) == 1): # checks to see if all elements of row 2 are same = win
            win = True
    if "1" not in set(y3): # makes sure all cells in row 3 are being used by X or O
        if (len(set(y3)) == 1): # checks to see if all elements of row 3 are same = win
            win = True

    if "1" not in set(x1): # makes sure all cells in column 1 are being used by X or O
        if (len(set(x1)) == 1): # checks to see if all elements of column 1 are same = win
            win = True
    if "1" not in set(x2): # makes sure all cells in column 2 are being used by X or O
        if (len(set(x2)) == 1): # checks to see if all elements of column 2 are same = win
            win = True
    if "1" not in set(x3): # makes sure all cells in column 3 are being used by X or O
        if (len(set(x3)) == 1): # checks to see if all elements of column 3 are same = win
            win = True

    if "1" not in set(z1): # makes sure all cells in diagonal 1 are being used by X or O
        if (len(set(z1)) == 1): # checks to see if all elements of diagonal 1 are same = win
            win = True
    if "1" not in set(z2): # makes sure all cells in diagonal 2 are being used by X or O
        if (len(set(z2)) == 1): # checks to see if all elements of diagonal 2 are same = win
            win = True
    
    return(win)
    
    


seedBlank = 111111111
seedBlankList = [(1,1,1),(1,1,1),(1,1,1)]

turnRound = 0
seedOutput = 0
i = 0
winner = 0 # can either be 0,1 or 2 (1 for X, 2 for 0)

while True == True:
    i += 1

    if i < 10: # checks to see if within round range (9 rounds for tic tac toe)
        if seedOutput == 0: # checks to see if its the first round, if so use blank seed
            seedInput = seedBlank
        else:
            seedInput = seedOutput

        seedList = seedNumToList(seedInput) # conversion for printGrid
        seedOutput = printGrid(seedInput, i) # prints the grid 

        turnIndex = (i % 2) + 1 # flips between 2 and 3 for the indices of gridCell which are X and O
        turnSymbol = (gridCell[turnIndex]).strip(' ') # gets symbol of current turn (X or O)
        turnSymbolPrevious = (gridCell[((i - 1) % 2) + 1]).strip(' ') # gets symbol of previous turn

        if 'redo' in locals():
            del redo
            print("You cannot overwrite!")

        if (seedWon(seedList) == False):
            coordsInput = [x for x in int(input(f"{turnSymbol}'s Turn (yx): "))]
        else:
            print(f"{turnSymbolPrevious} has won!")
            break
        # takes input from user as to where they want to place

        if int((seedList[int(coordsInput[0]) - 1])[int(coordsInput[1]) - 1]) == 1: # checks to see if selected index is not used by X or O (prevents overwriting)
            (seedList[int(coordsInput[0]) - 1])[int(coordsInput[1]) - 1] = turnIndex + 1
        else:
            redo = True
            i -= 1
        # gets the grid cell in which the user selected and changes it index of user's symbol (2 or 3 for X or O [uses gridCell])

        seedOutput = seedListToNum(seedList) # conversion for printGrid
        # converts previous seed into new seed using user input
    else:
        printGrid(seedOutput, i)
        print("Game ends in a TIE")
        break
