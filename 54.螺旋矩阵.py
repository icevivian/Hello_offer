#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]
        m = len(matrix)
        n = len(matrix[0])
        res = []
        left, right, top, bottom = 0, n-1, 0, m-1
        while left<=right and top<=bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            if left<right and top<bottom:
                for i in range(right-1, left-1,-1):
                    res.append(matrix[bottom][i])
                for i in range(bottom-1, top,-1):
                    res.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return res
# @lc code=end

