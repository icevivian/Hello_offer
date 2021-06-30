#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board 表示路径，row表征是否达到结束条件
        board = [['.' for i in range(n)] for j in range(n)]
        self.res = []
        row = 0
        self.backtrack(board, row)
        return self.res

    def backtrack(self, board, row):
        n = len(board)
        if row == n:
            self.res.append([''.join(board[i]) for i in range(n)])
            return
        for col in range(n):
            if not self.isvalid(board, row, col):
                continue
            board[row][col]='Q'
            self.backtrack(board, row+1)
            board[row][col]='.'
    
    def isvalid(self, board, row, col):
        # 判断是否在同一列有皇后
        for i in range(row):
            if board[i][col]=='Q':
                return False
        # 判断右上斜对角
        j = col
        for i in range(row-1,-1,-1):
            j = j + 1
            if j == len(board):
                break
            if board[i][j]=='Q':
                return False
        # 判断左上斜对角
        j = col
        for i in range(row-1,-1,-1):
            j = j-1
            if j == -1:
                break
            if board[i][j]=='Q':
                return False
        return True
# @lc code=end

