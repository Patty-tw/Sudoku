## Objectives 
- To demonstrate the ability to implement algorithms using basic data structure ad operations on them 
- To gain experiece in designing an algorithm for a given problem description and implementing that algorithm in Python 
- To demonstrate an understanding of complexity, and to the ability to implement algorithms of a given complexity

## Functions 

### grid_from_file(file_name): 
Reads in a file containing a sudoku grid and returns the contents of the file as a Python-readable table

### subgrid_values(grid, row, column):
Takes a *n x n* sudoku grid, a row coordinate, and a column coordinate, and returns a list containing the *n* values of the subgrid that the item at the coordinate belongs to

### valid_entry(grid, num, row, column):
Determines whether a particular value can be entered at a particular location in a valid grid, while maintaining validity 

### options(grid, row):

### grids_augmented_in_row(grid, num, r):
Returns the complete list of valid augmented grids, where each grid contains *num* in row *r*

### available(grid, num):

### grid_augmented_with_number(grid, num):
Returns a list of valid *n x n* gridsm where each grid contains *n nums*

### solve_sudoku_grid(grid):
Finds the solution for a given sudoku 


