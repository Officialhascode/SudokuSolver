def print_grid(grid):
    """Print the Sudoku grid in a readable format"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def find_empty_location(grid):
    """Find an empty cell in the grid (represented by 0)"""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, column
    return None

def is_valid(grid, num, pos):
    """Check if placing 'num' at 'pos' is valid"""
    # Check row
    if num in grid[pos[0]]:
        return False
    
    # Check column
    if num in [grid[i][pos[1]] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking"""
    empty = find_empty_location(grid)
    
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  # Backtrack
    
    return False

def main():
    """Main function to handle input and display"""
    print("SUDOKU SOLVER")
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells)")
    
    # Initialize empty grid
    grid = []
    for i in range(9):
        while True:
            row = input(f"Row {i+1} (9 numbers separated by spaces): ").split()
            if len(row) == 9:
                try:
                    row = [int(num) for num in row]
                    grid.append(row)
                    break
                except ValueError:
                    print("Please enter numbers only (0-9)")
            else:
                print("Please enter exactly 9 numbers separated by spaces")
    
    print("\nYour puzzle:")
    print_grid(grid)
    
    if solve_sudoku(grid):
        print("\nSolved Sudoku:")
        print_grid(grid)
    else:
        print("\nNo solution exists for this puzzle")

if __name__ == "__main__":
    main()