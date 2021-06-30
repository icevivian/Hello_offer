#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trace = []
        self.res = []
        self.len = len(nums)
        self.backtrace(trace, nums)
        return self.res
    def backtrace(self, trace, nums):
        if len(trace)==self.len:
            self.res.append(list(trace))
            return
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            trace.append(nums[i])
            self.backtrace(trace, nums[:i]+nums[i+1:])
            trace.pop()
            
# @lc code=end

