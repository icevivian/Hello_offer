#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = m-1
        col = 0
        while row >=0 and col<=n-1:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                row -= 1
            else:
                col += 1
        return False
# @lc code=end

