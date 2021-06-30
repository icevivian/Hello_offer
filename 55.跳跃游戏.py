#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        farest = 0
        for i in range(n-1):
            farest = max(farest, i+nums[i])
            if farest <= i:   
                return False   #说明nums[i]=0，跳不动了
        return farest>=n-1
# @lc code=end

