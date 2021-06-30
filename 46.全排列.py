#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        trace = []
        self.res = []
        self.backtrace(trace, nums)
        return self.res

    def backtrace(self, trace, nums):
        if len(trace) == len(nums):
            self.res.append(list(trace))
            return 
        for i in range(len(nums)):
            if nums[i] in trace:
                continue
            trace.append(nums[i])
            self.backtrace(trace, nums)
            trace.pop()
        

# @lc code=end

