#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        trace = []
        self.res = []
        self.backtrace(trace, 0, candidates, target)
        return self.res
    def backtrace(self, trace, start, candidates, target):
        if sum(trace) > target:
            return
        if sum(trace) == target:
            self.res.append(list(trace))
        for i in range(start, len(candidates)):
            trace.append(candidates[i])
            self.backtrace(trace, i, candidates, target)
            trace.pop()



# @lc code=end

