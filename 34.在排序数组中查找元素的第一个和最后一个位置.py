#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums)-1
        while left <=right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                right = mid-1
            elif nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
        if left>=len(nums) or nums[left]!=target:  # 当要搜索的词比nums[-1]大的时候，left=len(nums),其他情况下，判断nums[left]即可
            return [-1,-1]
        first = left
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
        second = right
        return [first, second]
# @lc code=end

