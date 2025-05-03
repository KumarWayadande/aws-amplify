def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
    # If all queens are placed, print the solution
    if row == n:
        print_board(board, n)
        return True
    
    res = False
    # Try placing the queen in all columns of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            res = solve_n_queens(board, row + 1, n) or res  # Recur to place the next queen
            board[row] = -1  # Backtrack
    return res

def print_board(board, n):
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))
    print()

def n_queens_backtracking(n):
    board = [-1] * n  # Initialize board with no queens placed
    if not solve_n_queens(board, 0, n):
        print("Solution does not exist")

# Example usage:
n = 8
n_queens_backtracking(n)
