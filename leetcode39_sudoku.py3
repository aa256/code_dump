from typing import Set, Tuple

class Solution:

    def row_vals(i):
        return [v for v in self.board[i] if v != "."]

    def col_vals(j):
        return [self.board[i][j] for i in range(9) if self.board[i][j] != "."]

    def sqr_vals(i,j):
        sqr = [self.board[3*i+k%3][3*j+k//3] for k in range(9)]
        return [v for v in sqr if v != "."]

    def solveSudokuHelper(self) -> bool:
        """Returns true if we find a solution"""
        print("here")
        print(self.blanks)
        print("board")
        for r in self.board:
            print(r)
        if len(self.blanks) == 0:
            return True
        best = (-1,-1)
        bestChoiceSize = 10
        bestConstraintSet = set()
        for b in self.blanks:
            i,j = b
            b_cons = self.row_vals[i].union(
                    self.col_vals[j]).union(
                        self.sqr_vals[i//3, j//3])
            choiceSize = 9-len(b_cons)
            if choiceSize <= 0:
                print("Bad state at {}".format(b))
                return False
            if choiceSize < bestChoiceSize:
                bestChoiceSize = choiceSize
                best = b
                bestConstraintSet = b_cons
        # Try each possible choice.
        for choice in range(1,10):
            if str(choice) in bestConstraintSet:
                continue
            choice = str(choice)
            print("choice")
            print(best, choice, bestConstraintSet)
            # Remove choice from blank set and update state.
            self.blanks.remove(best)
            i,j=best
            self.board[i][j] = choice
            self.row_vals[i].add(choice)
            self.col_vals[j].add(choice)
            self.sqr_vals[i//3, j//3].add(choice)
            if self.solveSudokuHelper():
                return True
            # Need to back track.
            print("removing choice")
            print(best, choice, bestConstraintSet)
            self.blanks.add(best)
            self.board[i][j] = "."
            self.row_vals[i].remove(choice)
            self.col_vals[j].remove(choice)
            self.sqr_vals[i//3, j//3].remove(choice)
        print("We've made a terrible mistake")
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row_vals = {i:set() for i in range(9)}
        self.col_vals = {i:set() for i in range(9)}
        self.sqr_vals = {(i%3, i//3):set() for i in range(9)}
        #self.blank_cons = dict()
        self.blanks = set()
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    #self.blank_cons[(i,j)] = set()
                    self.blanks.add((i,j))
                    continue
                self.row_vals[i].add(v)
                self.col_vals[j].add(v)
                self.sqr_vals[(i//3,j//3)].add(v)
        self.solveSudokuHelper()
        return

        