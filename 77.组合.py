#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        trace = []
        self.backtrack(trace, 0, k, n)
        return self.res
    
    def backtrack(self, trace, start, k, n):
        if len(trace) == k:
            self.res.append(list(trace))
            return
        for i in range(start, n):
            trace.append(i+1)
            self.backtrack(trace, i+1, k, n)
            trace.pop()
# @lc code=end

