#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        left, right = 0, n-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[mid] and nums[mid]==nums[right]:
                left+=1
                right-=1
            elif nums[mid]>=nums[left]: # 先判断哪一半有序
                if target>=nums[left] and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target > nums[mid] and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False

# @lc code=end

