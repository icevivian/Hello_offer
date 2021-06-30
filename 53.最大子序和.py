#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [-100001 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i], nums[i])
        return max(dp)
# @lc code=end

