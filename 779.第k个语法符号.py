#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k <= 2**(n-2):   # python中用**来表示幂
            return self.kthGrammar(n-1,k)
        else:
            return self.kthGrammar(n-1, k-2**(n-2))^1  # ^在python中是异或的意思
# @lc code=end

