#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        num = 1
        while left<=right and top<=bottom:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            for i in range(top+1, bottom+1):
                matrix[i][right] = num
                num += 1
            if left<right and top<bottom:
                for i in range(right-1, left-1,-1):
                    matrix[bottom][i] = num
                    num += 1
                for i in range(bottom-1, top,-1):
                    matrix[i][left] = num
                    num += 1
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return matrix
# @lc code=end

