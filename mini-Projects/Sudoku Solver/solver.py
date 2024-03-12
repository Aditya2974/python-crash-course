from pprint import pprint

def find_empty_place(puzzle):

    for row in range(9):
        for col in range(9):
            if(puzzle[row][col] == -1):
                return row,col
    
    return None,None

def is_valid(puzzle,guess,row,col):
    #Figuring out if the guess is a valid guess or not:

    row_vals = puzzle[row]

    if guess in row_vals:
        return False
    
    col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]

    if guess in col_vals:
        return False
    
    #We want to get where the 3by3 matrix starts :
    
    row_start = (row//3)*3
    col_start = (col//3)*3
    
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
            
    
    return True


def solve_sudoku(puzzle):
    # Solve using backtracking : 

    row,col = find_empty_place(puzzle)

    if row is None:
        return True
    
    # If there is a place to keep the number guess it : 
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            # Place that guess on the puzzle 
            puzzle[row][col] = guess
            # Recursively calling this function:
            if solve_sudoku(puzzle):
                return True
            
        # Guess is wrong:
        puzzle[row][col] = -1
    
    # If none of them work It is not solvable
    return False


example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

print("Main Sudoku Board")
print(example_board)

print("Is this puzzle solvable ?")
if solve_sudoku(example_board):
    print("Yes , it is solvable")