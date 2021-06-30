#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        trace = []
        self.backtrack(trace, 0, nums)
        return self.res
    
    def backtrack(self, trace, start, nums):
        self.res.append(list(trace))
        for i in range(start, len(nums)):
            if i>start and nums[i]==nums[i-1]: # 剪枝，当当前数已经被加入到队列中时不重复加入
                continue
            trace.append(nums[i])
            self.backtrack(trace, i+1, nums)
            trace.pop()
# @lc code=end

