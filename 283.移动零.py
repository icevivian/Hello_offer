#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow += 1
            fast+=1
        for i in range(slow, len(nums)):
            nums[i]=0
        return nums
# @lc code=end

