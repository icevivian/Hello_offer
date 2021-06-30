#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]: # 说明l～mid之间有序
                if target>=nums[l] and target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target>nums[mid] and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1


# @lc code=end

