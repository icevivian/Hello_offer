#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        n = len(nums)
        # dp[i][j]表示对前i个物品能否刚好装满重量为j的背包
        dp = [[False for i in range(target+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(target+1):
                if j-1 == -1:
                    dp[i][j] = True
                    continue
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[n][target]
# @lc code=end

