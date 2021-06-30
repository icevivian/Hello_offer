#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        pos = 0
        while pos<len(nums):
            value = nums[pos]
            ret = self.threeSum(nums, pos+1, target-value)
            for sub in ret:
                res.append(list([value]+sub))
            while pos<len(nums) and nums[pos]==value:
                pos += 1
        return res

    def threeSum(self, nums, start, target):
        res = []
        pos = start
        while pos<len(nums):
            value = nums[pos]
            ret = self.twoSum(nums, pos+1, target-value)
            for sub in ret:
                res.append(list([value]+sub))
            while pos<len(nums) and nums[pos]==value:
                pos += 1
        return res

    def twoSum(self, nums, start, target):
        res = []
        l = start
        r = len(nums)-1
        while r>l:
            left = nums[l]
            right = nums[r]
            if left+right == target:
                res.append(list([left, right]))
                while l<r and nums[l]==left:
                    l += 1
                while l<r and nums[r] == right:
                    r -= 1
            elif left+right > target:
                while l<r and nums[r] == right:
                    r -= 1
            else:
                while l<r and nums[l]==left:
                    l += 1
        return res
    




# @lc code=end

