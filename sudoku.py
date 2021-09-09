from copy import deepcopy

# Part A
def grid_from_file(file_name):
    out_list = 0
    graph = []
    f = open(file_name)
    for line in f:
        #line = line.rstrip('\n').split(',')
        print(line)
        graph.append(line)
    f.close()

    matrix = []
    for _ in range(len(graph)):
        list = [None] * len(graph)
        matrix.append(list)

    for list in matrix:
        for in_list in range(len(list)):
            if graph[out_list][in_list].isalpha() == False:
                matrix[out_list][in_list] = int(graph[out_list][in_list])
            else:
                matrix[out_list][in_list] = graph[out_list][in_list]
            in_list += 1
        out_list += 1

    return matrix
    

# Part B
def subgrid_values(grid, row, col): #adapted from assignment sheet 
    val = []
    n = int(len(grid)**0.5)
    r = (row//n)*n
    c = (col//n)*n
    for i in range(r, r+n):
        for j in range(c, c+n):
            val.append(grid[i][j])
    return val


def valid_entry(grid, num, r, c):
    while 0 < num <= len(grid) and 0 <= r < len(grid) and 0 <= r < len(grid):
        if grid[r].count(num) > 0:
            return False
        if subgrid_values(grid, r, c).count(num) > 0:
            return False
        for row in range(len(grid)):
            if grid[row][c] == num:
                return False
        return True


# Part C
def options(grid, row):
    opt = []
    for i in range(len(grid[row])):
        if grid[row][i] == 'x':
            opt.append(i)
    return opt


def grids_augmented_in_row(grid, num, r):
    poss = []
    if num in grid[r]:
        return grid

    else:
        for i in options(grid, r):
            copy_grid = deepcopy(grid)

            if valid_entry(grid, num, r, i):
                copy_grid[r][i] = num
                poss.append(copy_grid)

        return poss


# Part D
def available(grid, num):
    res = []
    for i in range(len(grid)):
        if num not in grid[i]:
            res.append(i)
    return res


def grids_augmented_with_number(grid, num):
    #function code from Lecture 17, slide 42
    check_llst = all(num in i for i in grid)
    if check_llst:
        return grid

    else:
        res = []
        for r in available(grid, num):
            for nested_lst in grids_augmented_in_row(grid, num, r):
                res += grids_augmented_with_number(nested_lst, num)
            return res


# Part E
def solve_sudoku_grid(grid):
    #function code from Lecture 17, slide 42
    if not any('x' in i for i in grid):
        return grid
    else:
        res = []
        for num in range(len(grid)):
            for r in available(grid, num+1):
                for nested_lst in grids_augmented_in_row(grid, num+1, r):
                    res += solve_sudoku_grid(nested_lst)
                return res

    

def solve_sudoku(file_name):
    grid = grid_from_file(file_name)
    return solve_sudoku_grid(grid)


