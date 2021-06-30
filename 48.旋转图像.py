#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return matrix
        for k in range(n-1):
            a1, a2, a3, a4 = matrix[0][k],matrix[k][n-1],matrix[n-1][n-1-k],matrix[n-1-k][0]
            matrix[k][n-1] = a1
            matrix[n-1][n-1-k] = a2
            matrix[n-1-k][0] = a3
            matrix[0][k] = a4
        matrix2 = [x[1:n-1] for x in matrix[1:n-1]]
        m = self.rotate(matrix2)
        for i in range(len(m)):
            matrix[1+i][1:n-1] = m[i]
        return matrix

# @lc code=end

