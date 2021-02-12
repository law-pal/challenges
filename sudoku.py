grid1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

grid = [['.', '.', '.', '.', '2', '.', '8', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

def sudoku(grid):
   """
   Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.
   Implements an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
   """
   # Empty sets for row, column, and 3x3 grid.
   row_set = set()
   column_set = set()
   grid_three_set = set()
   for i in range(len(grid)):
      for j in range(len(grid)):
         if grid[i][j] != '.':
            # value for each row in the grid.
            row_index = (i, grid[i][j])
            # value for each column on the grid.
            column_index = (j, grid[i][j])
            # value for each 3x3 grid
            by_three_index = (i // 3, j // 3, grid[i][j])
            # Check if the values of rows, columns and 3x3 grid already exist in their respective sets.
            if row_index in row_set or column_index in column_set or by_three_index in grid_three_set:
               return False
            row_set.add(row_index)
            column_set.add(column_index)
            grid_three_set.add(by_three_index)
   return True

print(sudoku(grid))

