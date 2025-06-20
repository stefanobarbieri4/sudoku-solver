class Board():
    def __init__(self, input_data):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.input_data = input_data
        self.load_grid()

    def load_grid(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = int(self.input_data[i * 9 + j])
    
    def display(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                val = self.grid[i][j]
                print(val if val != 0 else ".", end=" ")
            print()


class SudokuSolver():
    def __init__(self, board):
        self.board = board

    def board_check(self, row, col, num):
        grid = self.board.grid

        #Check if row and column have 1-9
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        
        #Check if 3x3 grid has 1-9
        corner_row, corner_col = 3 * (row // 3), 3 * (col // 3)
        
        for i in range(3):
            for j in range(3):
                if grid[corner_row + i][corner_col + j] == num:
                    return False
        
        return True

    def backtrack_solve(self):
        grid = self.board.grid
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1,10):
                        if self.board_check(row, col, num):
                            grid[row][col] = num
                            if self.backtrack_solve():
                                return True
                            grid[row][col] = 0
                    return False
        return True 
                     
                        
if __name__ == "__main__":
    puzzle_str = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    sudoku = Board(puzzle_str)

    print("Original Sudoku:")
    sudoku.display()

    solver = SudokuSolver(sudoku)
    if solver.backtrack_solve():
        print("\nSolved Sudoku:")
        sudoku.display()
    else:
        print("No solution found.")
