#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float('INF')
        i = 0
        while i<len(nums):
            value = nums[i]
            absres = self.twosumCloset(nums, i+1, target-value)
            res = res if abs(res)<abs(absres) else absres
            while i<len(nums) and nums[i]==value:
                i += 1
        return target+res
    
    def twosumCloset(self, nums, start, target):
        r = len(nums)-1
        l = start
        res = float('INF')
        while r>l:
            left = nums[l]
            right = nums[r]
            if left+right == target:
                return 0
            elif left+right > target:
                v = left+right-target
                r -= 1
            else:
                v = left+right-target
                l += 1
            res = res if abs(res)<abs(v) else v
        return res


# @lc code=end

