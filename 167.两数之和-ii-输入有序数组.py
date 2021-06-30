#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 只要数组有序，就应该想到双指针技巧。
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right]==target:
                return left+1, right+1
            if numbers[left]+numbers[right] > target:
                right -= 1
            if numbers[left]+numbers[right] < target:
                left += 1
# @lc code=end

