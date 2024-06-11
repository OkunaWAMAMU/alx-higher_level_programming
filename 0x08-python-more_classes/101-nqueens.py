#!/usr/bin/python3
import sys


def solve(N):
    def is_safe(board, row, col):
        return all(
            board[i] != col and
            board[i] + i != col + row and
            board[i] - i != col - row
            for i in range(row)
        )

    def place_queens(board, row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(board, row + 1)

    solutions = []
    place_queens([0] * N, 0)
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve(N)
