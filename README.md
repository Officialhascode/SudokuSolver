# Sudoku Solver 🧩

## Description ⌨️
A Python implementation of a Sudoku puzzle solver using backtracking algorithm.

## Features ✨
- Solves 9×9 Sudoku puzzles using backtracking
- Handles user input for puzzle entry
- Validates Sudoku rules (no duplicates in rows, columns, or 3×3 boxes)
- Clear visualization of the solved puzzle
- Lightweight with no external dependencies

## Algorithm 🧠
The solver uses recursive backtracking:
1. Finds the next empty cell (marked with 0)
2. Attempts to place digits 1-9 in the cell
3. Checks if the digit is valid according to Sudoku rules
4. Recursively attempts to solve the rest of the puzzle
5. Backtracks if no valid digit is found

## Example 📊
If the user inputs:<br/>

Enter Row 1 (9 numbers separated by spaces): 5 3 0 0 7 0 0 0 0<br/>
Enter Row 2 (9 numbers separated by spaces): 6 0 0 1 9 5 0 0 0<br/>
Enter Row 3 (9 numbers separated by spaces): 0 9 8 0 0 0 0 6 0<br/>
Enter Row 4 (9 numbers separated by spaces): 8 0 0 0 6 0 0 0 3<br/>
Enter Row 5 (9 numbers separated by spaces): 4 0 0 8 0 3 0 0 1<br/>
Enter Row 6 (9 numbers separated by spaces): 7 0 0 0 2 0 0 0 6<br/>
Enter Row 7 (9 numbers separated by spaces): 0 6 0 0 0 0 2 8 0<br/>
Enter Row 8 (9 numbers separated by spaces): 0 0 0 4 1 9 0 0 5<br/>
Enter Row 9 (9 numbers separated by spaces): 0 0 0 0 8 0 0 7 9<br/><br/>

5 3 0 |0 7 0 |0 0 0<br/>
6 0 0 |1 9 5 |0 0 0<br/>
0 9 8 |0 0 0 |0 6 0<br/>
------+------+-----<br/>
8 0 0 |0 6 0 |0 0 3<br/>
4 0 0 |8 0 3 |0 0 1<br/>
7 0 0 |0 2 0 |0 0 6<br/>
------+------+-----<br/>
0 6 0 |0 0 0 |2 8 0<br/>
0 0 0 |4 1 9 |0 0 5<br/>
0 0 0 |0 8 0 |0 7 9<br/><br/>

Output: Solved Puzzle<br/>
5 3 4 |6 7 8 |9 1 2<br/> 
6 7 2 |1 9 5 |3 4 8<br/>
1 9 8 |3 4 2 |5 6 7<br/> 
------+------+-----<br/>
8 5 9 |7 6 1 |4 2 3<br/> 
4 2 6 |8 5 3 |7 9 1<br/>
7 1 3 |9 2 4 |8 5 6<br/>
------+------+-----<br/>
9 6 1 |5 3 7 |2 8 4<br/>
2 8 7 |4 1 9 |6 3 5<br/>
3 4 5 |2 8 6 |1 7 9<br/>


