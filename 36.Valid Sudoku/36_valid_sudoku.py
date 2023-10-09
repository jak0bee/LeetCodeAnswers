class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Solution also posted on LeetCode
        # In this solution, we'll validate the Sudoku board by checking rows, columns, and boxes.
        # We use a hashset to keep track of seen numbers. A hashset helps in O(1) lookups to check duplicates.
        # As the board size is fixed (9x9), time and space complexity of this solution is O(1).

        hashset = set()

        # Check for each row and column
        for i in range(9):
            hashset.clear()
            for a in range(9):
                # Check the rows
                if board[i].count(board[i][a]) > 1 and board[i][a] != ".":
                    return False
                tmp = board[a][i]
                # Check the columns
                if tmp == ".":
                    continue
                if tmp in hashset:
                    return False
                hashset.add(tmp)

        # Check for each 3x3 box
        for box_row in range(3):
            for box in range(3):
                hashset.clear()
                for column in range(3):
                    for row in range(3):
                        tmp = board[row + 3 * box_row][column + 3 * box]
                        if tmp == ".":
                            continue
                        if tmp in hashset:
                            return False
                        hashset.add(tmp)

        return True
