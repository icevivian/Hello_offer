#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        self.memo = dict()
        return self.dp(k ,n)
        
    def dp(self, k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k,n) in self.memo:
            return self.memo[(k,n)]
        res = float('INF')
        for i in range(1, n+1):
            res = min(res, max(self.dp(k, n-i), self.dp(k-1, i-1))+1)
        self.memo[(k,n)]=res
        return res
# @lc code=end

