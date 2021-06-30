#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        jump = 0
        farest = 0
        for i in range(len(nums)-1):
            farest = max(farest, i+nums[i])
            if i == end:
                jump += 1
                end = farest           
        return jump
# @lc code=end

