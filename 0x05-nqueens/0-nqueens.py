#!/usr/bin/python3
""" N-Queens Problem Solver """

import sys

class NQueenSolver:
    """ Class to solve the N-Queens problem """

    def __init__(self, size):
        """ Initialize the solver with board size """
        self.size = size
        self.board = [0] * (size + 1)
        self.solutions = []

    def is_valid_position(self, queen_index, column):
        """ Check if a queen can be placed at (queen_index, column) """
        for prev_queen in range(1, queen_index):
            if (self.board[prev_queen] == column or
                abs(self.board[prev_queen] - column) == abs(prev_queen - queen_index)):
                return False
        return True

    def solve_n_queens(self, current_queen):
        """ Place queens on the board starting from the current_queen """
        for column in range(1, self.size + 1):
            if self.is_valid_position(current_queen, column):
                self.board[current_queen] = column
                if current_queen == self.size:
                    self._store_solution()
                else:
                    self.solve_n_queens(current_queen + 1)
        return self.solutions

    def _store_solution(self):
        """ Store a solution in the required format """
        solution = [[i - 1, self.board[i] - 1] for i in range(1, self.size + 1)]
        self.solutions.append(solution)

def main():
    """ Main function to handle input and output """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueenSolver(size)
    solutions = solver.solve_n_queens(1)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
