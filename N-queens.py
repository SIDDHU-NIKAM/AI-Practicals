def is_safe(row, col, board):
    # Check the diagonal
    irow, icol = row, col
    while irow >= 0 and icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        irow -= 1
        icol -= 1

    irow, icol = row, col
    while irow < len(board) and icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        irow += 1
        icol -= 1

    # Check the row
    irow, icol = row, col
    while icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        icol -= 1

    return True

def solve_n_queens(n):
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    find_board(n, solutions, board, 0)
    return solutions

def find_board(n, solutions, board, col):
    if col == n:
        solution = []
        for row in board:
            solution.append(''.join(row))
        solutions.append(solution)
        return

    for row in range(n):
        if is_safe(row, col, board):
            board[row][col] = 'Q'
            find_board(n, solutions, board, col + 1)
            board[row][col] = '.'

if __name__ == '__main__':
    n = int(input("Enter the board size: "))
    solutions = solve_n_queens(n)

    for solution in solutions:
        for row in solution:
            for ch in row:
                print(ch, end=' ')
            print()
        print("---------------------------------------------------------------")
        print()

    print("Total possible solutions =", len(solutions))
