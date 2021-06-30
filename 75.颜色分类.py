#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        for i in range(n):
            if nums[i]==0:
                nums[i],nums[pos]=nums[pos],nums[i]
                pos+=1
        for i in range(pos, n):
            if nums[i]==1:
                nums[i],nums[pos]=nums[pos],nums[i]
                pos+=1
        return nums
# @lc code=end

