#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}
        return self.count(1,n)
    
    def count(self, left, right):
        sumvalue = 0
        if left > right:
            return 1
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        for i in range(left, right+1):
            l = self.count(left, i-1)
            r = self.count(i+1, right)
            sumvalue += l*r
        self.memo[(left, right)] = sumvalue
        return sumvalue

# @lc code=end

