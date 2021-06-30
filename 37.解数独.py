#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.backtrack(board, 0, 0)


    def backtrack(self, track, row, col):
        if row == 9:
            return track   # 停止条件

        if col == 9:       # 处理越界
            return self.backtrack(track, row+1, 0)

        if track[row][col] != '.':
            return self.backtrack(track, row, col+1)
        
        for i in range(1,10):
            if self.isvalid(track, row, col, str(i)):
                track[row][col] = str(i)
                res = self.backtrack(track, row, col+1)
                if res:  # 当存在一个可行解时即返回
                    return res
                track[row][col] = '.'

    def isvalid(self, track, row, col, i):
        for index in range(9):
            if track[index][col] == i:
                return False
            if track[row][index] == i:
                return False
            if track[(row//3)*3+index//3][(col//3)*3+index%3] == i:
                return False
        return True     
# @lc code=end

