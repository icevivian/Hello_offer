#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c]!='.' and not self.isValid(board, r, c):
                    print(r,c)
                    return False
        return True

    def isValid(self, board, r, c):
        value = board[r][c]
        for i in range(9):
            if i!=r and board[i][c] == value:
                return False
            if i!=c and board[r][i] == value:
                return False
            if i!=(r-(r//3)*3)*3+(c-(c//3)*3) and board[(r//3)*3+i//3][(c//3)*3+i%3] == value:
                return False
        return True

# @lc code=end

