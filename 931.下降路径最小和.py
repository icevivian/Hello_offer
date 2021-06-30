#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.n = len(matrix)
        # 初始化一个二维数组，千万不能用[[0]*5]*6
        self.memo = [[66666 for row in range(self.n)] for row in range(self.n)]
        res = float('INF')
        for j in range(self.n):   
            res = min(res, self.help(self.n-1, j))
        return res
        
    def help(self, i, j): # 函数输出为落到结束点为[i,j]位置的最小和
        if i < 0 or j <0 or j>=self.n or i>=self.n:   
            return 99999
        if i == 0:
            return self.matrix[i][j]
        if self.memo[i][j] != 66666:
            return self.memo[i][j]
        self.memo[i][j] = self.matrix[i][j]+min(self.help(i-1,j), self.help(i-1,j-1), self.help(i-1,j+1))
        return self.memo[i][j]       
# @lc code=end

