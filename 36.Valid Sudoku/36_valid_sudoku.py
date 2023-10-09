class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #lets first check the rows and columns
        hashset = set()
        for i in range(9):
            hashset.clear()
            for a in range(9):
                #check the rows
                if board[i].count(board[i][a]) > 1 and board[i][a] != ".":
                    return False
                tmp = board[a][i]
                #check the columns
                if tmp == ".":
                    continue
                if tmp in hashset:
                    return False
                hashset.add(tmp)
        #then let's check the squares
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