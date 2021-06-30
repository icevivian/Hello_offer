#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        trace = []
        self.res = []
        self.backtrace(trace, 0, candidates, target)
        return self.res
    def backtrace(self, trace, start, candidates, target):
        if sum(trace)>target:
            return
        if sum(trace)==target:
            self.res.append(list(trace))
        for i in range(start, len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue
            trace.append(candidates[i])
            self.backtrace(trace, i+1, candidates, target)
            trace.pop()

