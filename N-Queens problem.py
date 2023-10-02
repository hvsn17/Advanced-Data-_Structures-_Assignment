def solve_n_queens(N):
    def is_safe(board, row, col):
        # Check if no queens threaten the current cell
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < N and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def backtrack(board, row):
        if row == N:
            # All queens are placed successfully, add the solution
            solutions.append([''.join(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    backtrack(board, 0)

    return solutions

# Example usage
N = 4
solutions = solve_n_queens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()
